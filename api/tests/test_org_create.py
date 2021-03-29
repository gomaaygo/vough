import json

# Django imports
from django.test import TestCase

# Drf imports
from rest_framework import status
from rest_framework.test import APIClient

# Api imports 
from api.models import Organization


class TestOrgCreateApi(TestCase):
    def setUp(self):
        self.data = {
            "login": "instruct-br",
            "name": "Instruct",
            "score": 39
        }
        self.resp = self.client.post('/api/orgs/',
            data=json.dumps(self.data),
            content_type='application/json')
      

    def test_create_organization(self):
        self.assertEqual(self.resp.status_code, status.HTTP_201_CREATED)