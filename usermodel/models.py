from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    follows = models.ManyToManyField('self', symmetrical=False)
    def __str__(self):
        return self.email
