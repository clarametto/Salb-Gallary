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
    

class Category(models.Model):
    title = models.CharField(max_length=150)

    def save_category(self):
        self.save()

    def update_category(self, update):
        self.title = update
        self.save()

    def delete_category(self):
        self.delete()    

    @classmethod
    def get_category_id(cls,id):
        category_id = Category.objects.get(pk=id)
        return category_id

    def __str__(self):
        return self.title


