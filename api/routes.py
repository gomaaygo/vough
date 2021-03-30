# Django imports
from django.urls import include, path

# Drf imports
from rest_framework.routers import DefaultRouter

# Api imports 
from api.views import OrganizationViewSet, DocumentationView


routers = DefaultRouter()
routers.register(r'orgs', OrganizationViewSet, basename='org')

urlpatterns = [
    path('documentation/', DocumentationView.as_view()),
]

urlpatterns += routers.urls