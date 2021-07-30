# Django imports
from django.urls import include, path

# Drf imports
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

# Api imports 
from api.views import OrganizationViewSet, DocumentationView


routers = DefaultRouter()
routers.register(r'orgs', OrganizationViewSet, basename='org')

urlpatterns = [
    path('documentation/', DocumentationView.as_view()),
    path('login/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += routers.urls