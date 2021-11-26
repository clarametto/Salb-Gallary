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


class Photo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    posted_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()

    @classmethod
    def update_photo(cls,id,title,description,location,category, owner):
        update = cls.object.filter(id=id).update(title=title, description=description, location=location, category=category, owner=owner)
        return update
    
    @classmethod
    def get_all_photos(cls):
        photos = cls.object.all()
        return photos

    @classmethod
    def get_photo_id(cls,id): 
        phot_id = cls.object.filter(id=id).all()
        return phot_id

    @classmethod
    def filter_photo_by_location(cls,location):
        photos = cls.object.filter(location___title__icontains=location) 
        return location  

    @classmethod
    def filter_photo_by_categories(cls,category):
        photos = cls.object.filter(category___title__icontains=category) 
        return category 

    def __str__(self):
        return self.title

    
           



