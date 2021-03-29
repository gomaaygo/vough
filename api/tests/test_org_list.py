import json

# Django imports
from django.test import TestCase

# Drf imports
from rest_framework import status
from rest_framework.test import APIClient

# Api imports 
from api.models import Organization


class TestOrgListApi(TestCase):
    def setUp(self):
        self.organization1 = Organization.objects.create(
            login="instruct-br",
            name='Instruct',
            score=39)
        self.organization1.save()
        self.organization2 = Organization.objects.create(
            login="example2",
            name='Example 2',
            score=5)
        self.organization2.save()
        self.organization3 = Organization.objects.create(
            login="example3",
            name='Example 3',
            score=67)
        self.organization2.save()          
        self.resp = self.client.get('/api/orgs/')
        self.data = [{
            "login": "example3",
            "name": "Example 3",
            "score": 67
        },
        {
            "login": "instruct-br",
            "name": "Instruct",
            "score": 39
        },
        {
            "login": "example2",
            "name": "Example 2",
            "score": 5
        }
        ]

    def test_status_code(self):
        self.assertEqual(self.resp.status_code, status.HTTP_200_OK)

    def test_response(self):
        self.assertEqual(json.loads(self.resp.content), self.data)