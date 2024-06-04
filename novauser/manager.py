from django.contrib.auth.models import BaseUserManager
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.db import models
class CustomUserManager(BaseUserManager):

    # # Creates and saves a regular user with the given email and password.
    # def create_user(self, email, password=None, **extra_fields):
    #     if not email:
    #         raise ValueError("The Email field must be set")
    #     email = self.normalize_email(email)
    #     username = extra_fields.get('username')
    #     if username and self.model.objects.filter(username=username).exists():
    #         raise ValueError("The username already exists")
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user


    # # Creates and saves a superuser with the given email and password.
    # def create_superuser(self, email, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)

    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError('Superuser must have is_staff=True.')
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')

    #     return self.create_user(email, password, **extra_fields)

    def create_user(self, email, password=None, fname=None, lname=None, **extra_fields):
        if not email:
            raise ValueError("The Email field can't be empty!")
        email = self.normalize_email(email)
        username = extra_fields.get('username')
        if username and self.model.objects.filter(username=username).exists():
            raise ValueError("The username already exists")
        user = self.model(email=email, fname=fname, lname=lname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, fname=None, lname=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, fname, lname, **extra_fields)
    



    def get_active_sessions(user):
        """""
        # Get the current time
        current_time = timezone.now()

        # Query active sessions associated with the user
        active_sessions = Session.objects.filter(expire_date__gte=current_time, user_id=user.id)
        """""

        # Get the current time
        current_time = timezone.now()

        # Get the session model associated with the current database
        session_model = Session.objects.using(Session.objects.db)

        # Serialize the user's ID to match the session data format
        user_id_str = str(user.id)

        # Query active sessions associated with the user
        active_sessions = session_model.filter(expire_date__gte=current_time, session_data__contains=user_id_str)

        return active_sessions


class WishlistManager(models.Manager):
    def add_to_wishlist(self, ticker, user):
        wishlist_item, created = self.get_or_create(ticker=ticker, user=user)
        return wishlist_item, created

    def remove_from_wishlist(self, ticker, user):
        try:
            wishlist_item = self.get(ticker=ticker, user=user)
            wishlist_item.delete()
            return True
        except Wishlist.DoesNotExist:
            return False