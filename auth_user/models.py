from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    is_verified = models.BooleanField(default=False)
    username = None
    email = models.EmailField(unique=True)
    github_link = models.URLField(max_length=255)
    linkedin_link = models.URLField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class CodeGenery(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.IntegerField()

    def __str__(self):
        return f'{self.code}'
