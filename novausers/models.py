from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class Users(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # def __str__(self):
    #     return self.email
