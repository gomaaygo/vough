# Django imports
from django.shortcuts import get_object_or_404
from django.http import Http404

# Drf imports
from rest_framework import viewsets, status
from rest_framework.views import Response
from rest_framework.decorators import action

# Api imports 
from api import models, serializers
from api.integrations.github import GithubApi
from api.serializers import OrganizationSerializer
from api.models import Organization
from api.utils import get_score


class OrganizationViewSet(viewsets.ViewSet):
    """
        A viewset that provides create(), retrieve(), destroy()
        and list() actions.
    """

    def list(self, request):
        """
            View that lists all organizations with the highest 
            score for the smaller.
        """
        queryset = Organization.objects.all().order_by('-score')
        serializer = OrganizationSerializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request):
        """
            View that creates an organization instance.
        """
        organization = Organization(
            login=request.data['login'],
            name=request.data['name'],
            score=get_score(request.data['login'])
        )
        organization.save()
        serializer = OrganizationSerializer(organization)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        """
            View of details of an organization.
        """
        queryset = Organization.objects.all()
        organization = get_object_or_404(queryset, pk=pk)
        serializer = OrganizationSerializer(organization)
        return Response(serializer.data)


    def destroy(self, request, pk=None):
        """
            View of exclusion of an organization.
        """
        queryset = Organization.objects.all()
        organization = get_object_or_404(queryset, pk=pk)
        organization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        


list_all_organization = OrganizationViewSet.as_view({'get': 'list'})
organization_detail = OrganizationViewSet.as_view({'get': 'retrieve'})
organization_delete = OrganizationViewSet.as_view({'delete': 'destroy'})
create_organization = OrganizationViewSet.as_view({'post': 'create'})
