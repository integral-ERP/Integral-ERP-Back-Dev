from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# from user.models import User
# Register your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass