from django.db import models
from stdimage.models import StdImageField

import uuid
# from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, password, **extra_fields):
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password=None, **extra_fields):
        # extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(password, **extra_fields)

    def create_superuser(self, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser precisa ter is_superuser=True")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Staff precisa ter is_staff = True")

        return self._create_user(password, **extra_fields)


def get_file_path(_instace, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class CustomUsuario(AbstractUser):
    avatar = StdImageField(
        'Foto de perfil',
        blank=True,
        upload_to=get_file_path,)
    bio = models.CharField('bio', max_length=100, blank=True)
    is_staff = models.BooleanField("Membro da equipe", default=True)
    REQUIRED_FIELDS = ["first_name"]

    def __str__(self):
        return self.first_name

    objects = UsuarioManager()
