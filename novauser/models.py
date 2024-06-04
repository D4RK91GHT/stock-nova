from django.contrib.auth.models import AbstractUser
from django.db import models

from .manager import CustomUserManager, WishlistManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    fname = models.CharField(max_length=50, blank=True)
    lname = models.CharField(max_length=50, blank=True)

    # Use email as the username field
    USERNAME_FIELD = 'email'
    # Make email and password required fields
    REQUIRED_FIELDS = ['password']
    objects = CustomUserManager()
    

class Wishlist(models.Model):
    id          = models.AutoField(primary_key=True)
    ticker      = models.CharField(max_length=50)
    user        = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    added_on    = models.DateTimeField(auto_now_add=True)

    objects = WishlistManager()
    
    def __str__(self):
        return f'{self.user.email} - {self.ticker}'