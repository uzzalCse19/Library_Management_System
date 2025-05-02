from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager  
class User(AbstractUser):
    LIBRARIAN = 1
    MEMBER = 2

    ROLE_CHOICES = (
        (LIBRARIAN, 'Librarian'),
        (MEMBER, 'Member'),
    )

    username = None  
    email = models.EmailField(unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=MEMBER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  

    def __str__(self):
        return self.email

    @property
    def is_librarian(self):
        return self.role == self.LIBRARIAN
