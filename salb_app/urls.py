from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.home,name='homePage'),
  path('photos/',views.photos,name='allPhotos'),
  path('photo/<int:photo_id>',views.detail,name='photos_item.detail'),
  path('mombasa/',views.filter_mombasa_photos,name='mombasa'),
  path('nairobi/',views.filter_campus_nairobi,name='nairobi'),
  path('Johannesburg/',views.filter_Johannesburg_photos,name='Johannesburg'),
  path('narok/',views.filter_narok_photos,name='narok'),
  path('search/',views.search_photos_category, name='searchPhotos')
]

if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)