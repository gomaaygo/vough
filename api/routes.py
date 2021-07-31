# Django imports
from django.urls import include, path

# Drf imports
from rest_framework.routers import DefaultRouter

# Api imports 
from api.views import OrganizationViewSet


routers = DefaultRouter()
routers.register(r'orgs', OrganizationViewSet, basename='org')

urlpatterns = []

urlpatterns += routers.urls