from django.db import models
from django.core.validators import MinValueValidator


class Organization(models.Model):
    login = models.CharField(verbose_name='Login', max_length=255, primary_key=True)
    name = models.CharField(verbose_name='Nome da Organização', max_length=255)
    score = models.PositiveIntegerField(verbose_name='Score', blank=True, null=True)

    REQUIRED_FIELD = ['login', 'name']

    class Meta:
        verbose_name = 'organização'
        verbose_name_plural = 'organizações'


    def __str__(self):
        return self.name