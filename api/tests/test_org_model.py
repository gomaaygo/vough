from django.test import TestCase

from api.models import Organization


class OrganizationModelTest(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(
            login="instruct-br",
            name='Instruct',
            score=39)
        self.organization.save()

    def test_create(self):
        self.assertTrue(Organization.objects.exists())

    def test_str(self):
        self.assertEqual('Instruct', str(self.organization))

    def test_login_field(self):
        self.assertEquals(self.organization.login, 'instruct-br')

    def test_name_field(self):
        self.assertEquals(self.organization.name, 'Instruct')

    def test_score_field(self):
        self.assertEquals(self.organization.score, 39)

    def test_login_not_can_be_null(self):
        field = Organization._meta.get_field('login')
        self.assertFalse(field.null)

    def test_name_not_can_be_null(self):
        field = Organization._meta.get_field('name')
        self.assertFalse(field.null)

    def test_score_null(self):
        field = Organization._meta.get_field('score')
        self.assertTrue(field.null)

    def test_score_blank(self):
        field = Organization._meta.get_field('score')
        self.assertTrue(field.blank)
