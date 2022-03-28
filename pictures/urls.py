from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.main,name = 'main'),
    path('search/', views.search_results, name='search_results'),
    
    path('location/', views.photo_location, name='photo_location'),
]

#serve uploaded images on the development server 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)