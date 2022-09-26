from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):

    # metodo para crear un usuario
    def _create_user(
        self, username, password, is_staff, is_superuser, is_active
    ):
        user = self.model(
            username=username,
            is_staff=is_staff,  # me dice si puede o no acceder al administrador
            is_superuser=is_superuser,  # me dice si es un super user es bool
            is_active=is_active,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    # metodo para crear  usuarios
    def create_user(self, username, password=None):
        return self._create_user(username, password, False, False, True)

    # metodo para crear super usuarios
    def create_superuser(self, username, password=None):
        return self._create_user(username, password, True, True, True)
