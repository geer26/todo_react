from django.contrib import admin
from .models import CustomUser, Group
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm, CustomGroupCreationForm

# Register your models here.

"""
class CustomUserCreation():
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'full_name']

class Customgroup():
    add_form = CustomGroupCreationForm
    model = Group
    list_display = ['name', 'description',]
    
"""

admin.site.register(CustomUser)
admin.site.register(Group)