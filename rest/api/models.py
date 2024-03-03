from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


# Create your models here.

class CustomUser(AbstractUser):
    
    username = None
    phone_number = models.CharField(max_length=120 , unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=150)
    user_profile = models.ImageField(upload_to="profile")
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    


