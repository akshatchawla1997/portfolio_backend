from rest_framework import serializers
from .models import Blogs, Experience, Education, Projects, Contact_Me, Send_Resume

class BlogSerializers(serializers.ModelSerializers):
    class Meta:
        model = Blogs
        fields = ['id', 'title', 'content', 'cover_photo', 'created_at', 'updated_at']

class ExperienceSerializers(serializers.ModelSerializers):
    class Meta:
        model = Experience
        fields = ['company_name', 'description', 'tech_stack', 'job_title', 'location', 'start_date', 'end_date']

class EducationSerializers(serializers.ModelSerializers):
    class Meta:
        model = Education
        fields = ['college_name', 'start_date','end_date','degree','logo', 'cgpa']

class ProjectsSerializers(serializers.ModelSerializers):
    class Meta:
        model = Projects
        fields = ['title','description', 'technologies_used', 'github_link', 'live_demo_link', 'image', 'created_at', 'updated_at']

    
class ContactMeSerializers(serializers.ModelSerializers):
    class Meta:
        model = Contact_Me
        fields = ['name', 'email', 'subject', 'message', 'created_at']

class SendResumeSerializers(serializers.ModelSerializers):
    class Meta:
        model = Send_Resume
        fields = ['email']