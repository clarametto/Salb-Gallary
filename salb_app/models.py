from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15,blank=True)

    def __str__(self):
        return self.first_name

    class meta:
        ordering = ['name']

    def save_owner(self):
        self.save()   

class Category(models.Model):
    title = models.CharField(max_length =50)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.title = update
        self.save()

    @classmethod
    def get_category_id(cls, id):
        category_id = Category.objects.get(pk = id)
        return category_id

    def __str__(self):
        return self.title

class Location(models.Model):
    title = models.CharField(max_length=100)  
    

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.title = update
        self.save()

    @classmethod
    def get_location_id(cls, id):
        location_id = Location.objects.get(pk = id)
        return location_id

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
    def update_photo(cls, id ,title,description ,owner, location, category):
        update = cls.objects.filter(id = id).update(title = title,description = description,owner=owner,location = location,category = category)
        return update

    @classmethod
    def get_all_photos(cls):
        photos = cls.objects.all()
        return photos

    @classmethod
    def get_photo_id(cls,id):
        photo_id = cls.objects.filter(id= id).all()
        return photo_id

    @classmethod
    def filter_photo_by_location(cls,location):
        photos = Photo.objects.filter(location__title__icontains=location)
        return location

    @classmethod
    def search_photos_by_category(cls,category):
        photos = Photo.objects.filter(category__title__icontains=category)
        return photos


    def __str__(self):
        return self.title
 