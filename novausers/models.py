from django.db import models
from django.utils import timezone # type: ignore

# Create your models here.
class RegisterUser(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    registration_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
