"""
Model Registry for users app.
"""

from django.contrib import admin
from .models import (
    User,
    UserRole
)

class UserAdmin(admin.ModelAdmin):
    """Admin regitration for User model."""
    list_display = (
        'first_name', 'last_name', 'email', 'username', 'role'
    )


class UserRoleAdmin(admin.ModelAdmin):
    """Admin registration for UserRole model."""
    list_display =  ['name']


admin.site.register(User, UserAdmin)
admin.site.register(UserRole, UserRoleAdmin)