from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email','age','address','avatar','phone']
