from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserAuthentication(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False, unique=True)
    location = models.CharField(max_length=150, blank=False)
    mobile_number = models.CharField(max_length=12, blank=False, unique=True)
