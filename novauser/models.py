from django.contrib.auth.models import AbstractUser
from django.db import models

from .manager import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    
    # Use email as the username field
    USERNAME_FIELD = 'email'
    # Make email and password required fields
    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()