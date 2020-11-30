from django.contrib.auth.models import User
from django.db import models
from website import settings


class UserProfile(User):
    photo = models.FileField(upload_to="media", blank=True, null=True, unique=False)
