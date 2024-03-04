"""
Models for user app.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)
from baseApp.models import BaseModel

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, first_name, last_name, username, email, password=None):
        """Create, save and return a new user."""

        if not email:
            ValueError("User must have an email address.")
        if not username:
            ValueError("User must have an username.")

        user = self.model(
            email = self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        """Create and return a superuser."""

        user = self.create_user(first_name, last_name, username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class UserRole(BaseModel):
    """Role for the users in the system."""
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class User(AbstractBaseUser, BaseModel):
    """User in the system."""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True