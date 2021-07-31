import json

# Django imports
from django.test import TestCase

# Drf imports
from rest_framework import status
from rest_framework.test import APIClient

# Api imports 
from api.models import Organization


class TestOrgDetailApi(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(
            login="instruct-br",
            name='Instruct',
            score=39)
        self.organization.save()
        self.resp = self.client.get('/api/orgs/instruct-br/')
        self.data = {
            "login": "instruct-br",
            "name": "Instruct",
            "score": 39
        }

    def test_status_code(self):
        self.assertEqual(self.resp.status_code, status.HTTP_200_OK)

    def test_response(self):
        self.assertEqual(json.loads(self.resp.content), self.data)


class TestOrgDetailFailedApi(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(
            login="instruct-br",
            name='Instruct',
            score=39)
        self.organization.save()
        self.resp = self.client.get('/api/orgs/gomaaygo/')
        self.data = {
            "detail": "Não encontrado."
        }

    def test_status_code(self):
        self.assertEqual(self.resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_response(self):
        self.assertEqual(json.loads(self.resp.content), self.data)