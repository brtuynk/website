from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin
from django.db import models


class UserProfile(User):
    photo = models.FileField(upload_to="media", blank=True, null=True, unique=False)
