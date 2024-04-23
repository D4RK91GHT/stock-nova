from django.contrib.auth.models import BaseUserManager
from django.contrib.sessions.models import Session
from django.utils import timezone

class CustomUserManager(BaseUserManager):

    # Creates and saves a regular user with the given email and password.
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        username = extra_fields.get('username')
        if username and self.model.objects.filter(username=username).exists():
            raise ValueError("The username already exists")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    # Creates and saves a superuser with the given email and password.
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)



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
