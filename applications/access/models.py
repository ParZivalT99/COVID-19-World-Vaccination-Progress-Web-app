# from random import choices
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import validate_slug
from django.db import models

# managers
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        "username",
        max_length=50,
        validators=[validate_slug],
        unique=True,)
    
    created_at = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    objects = UserManager()

    class Meta:
        verbose_name = "Register user"
        verbose_name_plural = "Register users"
        ordering = ["username"]

    def get_name(self):
        return self.username

