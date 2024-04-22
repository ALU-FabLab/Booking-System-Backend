"""
Admin site configuration
"""

from django.contrib import admin
from users import models
from django.utils.translation import gettext as translate_text
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    """
    The user model for admin
    """
    ordering = ['id']
    list_display = [
        'id', 'email', 'first_name', 'last_name',
        'is_active', 'is_staff', 'intake',
    ]
    readonly_fields = ['last_login', 'date_joined', 'date_modified']
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'password',
                )
            }
        ),
        (
            translate_text('Personal Info'),
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'short_bio',
                    'about_me',
                    'intake',
                    'course',
                    'professional_role',
                )
            }
        ),
        (
            translate_text('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (
            translate_text('Important dates'),
            {
                'fields': (
                    'last_login',
                    'date_joined',
                    'date_modified',
                )
            }
        )
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'first_name',
                    'last_name',
                    'short_bio',
                    'about_me',
                    'intake',
                    'course',
                    'professional_role',
                    'is_staff',
                    'is_active',
                    'is_superuser',
                )
            }
        ),
    )
