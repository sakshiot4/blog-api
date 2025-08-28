from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # Add any additional fields if needed
    name = models.CharField(null=True, blank=True, max_length=100)