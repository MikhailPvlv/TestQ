from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=90)
    birth_date = models.DateField(null=True)
    linkdn_link = models.URLField(max_length=300)
    github_link = models.URLField(max_length=300)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = CustomUserManager()

    def __str__(self):
        return self.email
