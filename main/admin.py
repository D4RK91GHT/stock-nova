from django.contrib import admin # type: ignore
from .models import  *

# Register your models here.
@admin.register(RegisterUser)
class RegisterUserAdmin(admin.ModelAdmin):
    pass
