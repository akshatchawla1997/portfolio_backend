# your_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogsViews, ExperienceViewSet, EducationViewSet, ProjectsViewSet, ContactmeViewSet

router = DefaultRouter()
router.register(r'blogs/', BlogsViews)
router.register(r'experiences/', ExperienceViewSet)
router.register(r'education/', EducationViewSet)
router.register(r'projects/', ProjectsViewSet)
router.register(r'contact/', ContactmeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
