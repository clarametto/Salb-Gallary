from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['name']
        
    def save_PersonalInfo(self):
        self.save()
