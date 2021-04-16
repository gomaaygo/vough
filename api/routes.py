# Django imports
from django.urls import include, path

# Drf imports
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

# Api imports 
from api.views import OrganizationViewSet, DocumentationView


routers = DefaultRouter()
routers.register(r'orgs', OrganizationViewSet, basename='org')

urlpatterns = [
    path('documentation/', DocumentationView.as_view()),
    path('login/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
]

urlpatterns += routers.urls