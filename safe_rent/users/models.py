from django.db import models
from django.contrib.auth.models import AbstractUser


# Creating User Models
class User(AbstractUser):
    #Extra fields 
    phone_number = models.CharField(max_length=14, unique=True, null=True, blank=True)
    is_landlord = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    address = models.CharField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username



