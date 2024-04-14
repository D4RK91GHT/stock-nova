# from django.contrib import admin

from django.contrib import admin # type: ignore
# Register your models here.
from .models import  *

# Register your models here.
@admin.register(RegisterUser)
class RegisterUserAdmin(admin.ModelAdmin):
    pass
