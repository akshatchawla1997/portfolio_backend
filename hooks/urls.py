from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogsViews

router = DefaultRouter
router.register(r'blogs/', BlogsViews)