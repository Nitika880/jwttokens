from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    gender = models.CharField(max_length=20)