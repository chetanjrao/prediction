from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Others')
    )
    mobile = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=0)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1)
    has_cancer = models.BooleanField(default=False)
    username = models.CharField(null=True, blank=True, max_length=12)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'mobile', 'username']