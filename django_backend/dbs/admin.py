from django.contrib import admin
from .models import CustomUser, Group
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm, CustomGroupCreationForm

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    fields = ('username', 'email')
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser


class CustomGroupAdmin(admin.ModelAdmin):
    add_form = CustomGroupCreationForm
    model = Group
    list_display = ['name', 'description', ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Group, CustomGroupAdmin)