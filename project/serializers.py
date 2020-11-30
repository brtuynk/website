from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from project import models
from project.models import Project
from django.contrib.auth.models import Group
from rest_framework.exceptions import ValidationError

from django.contrib.auth import get_user_model


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = [
            'id',
            'first_name',
            'country',
            'language',
            'surname',
            #'email',
        ]




class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
