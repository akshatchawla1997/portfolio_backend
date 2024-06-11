from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_photo = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    company_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    tech_stack = models.CharField(max_length=200)
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.job_title

class Education(models.Model):
    college_name = models.TextField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    degree = models.TextField(max_length=100)
    logo = models.TextField(max_length=200)
    cgpa = models.DecimalField(_("CGPA"), max_digits=5, decimal_places=2)

class Projects(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField()
    technologies_used = models.CharField(max_length=255)
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True, max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact_Me(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
class Send_Resume(models.Model):
    email = models.EmailField()