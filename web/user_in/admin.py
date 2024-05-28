from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name', 'contact')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name', 'contact',
                  'is_active', 'is_staff', 'is_superuser')


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'name', 'contact',
                    'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('name', 'contact')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'name', 'contact', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )
    search_fields = ('username', 'email', 'name', 'contact')
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)
