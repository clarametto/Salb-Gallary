from django.contrib import admin
from . models import PersonalInfo, Category, Location, Photo

# Register your models here.

admin.site.register(PersonalInfo)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Photo)

