from django.db import models


class Project(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True, unique=False)
    surname = models.CharField(max_length=100, blank=True, null=True, unique=False)
    country = models.CharField(max_length=100, blank=True, null=True, unique=False)
    language = models.CharField(max_length=300, blank=True, null=True, unique=False, default='English')
    #email = models.EmailField(max_length=100, default='common')
