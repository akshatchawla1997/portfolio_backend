from django.shortcuts import render
from rest_framework import viewsets
from .models import Blogs, Education, Experience, Projects, Contact_Me, Send_Resume
from .serializers import BlogSerializers, EducationSerializers, ExperienceSerializers, ProjectsSerializers,ContactMeSerializers, SendResumeSerializers
# Create your views here.


class BlogsViews(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializers

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializers

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializers

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializers

class ContactmeViewSet(viewsets.ModelViewSet):
    queryset = Contact_Me.objects.all()
    serializer_class = ContactMeSerializers

