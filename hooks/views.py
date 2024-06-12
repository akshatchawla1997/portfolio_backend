from django.shortcuts import render
from rest_framework import viewsets
from .models import Blogs, Education, Experience, Projects, Contact_Me, Send_Resume
from .serializers import BlogSerializers, EducationSerializers, ExperienceSerializers, ProjectsSerializers,ContactMeSerializers, SendResumeSerializers
# Create your views here.


class BlogsViews(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializers
