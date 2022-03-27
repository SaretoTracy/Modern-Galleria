from django.urls import path,register_converter
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .models import UrlDateConverter

urlpatterns = [
    path('',views.main,name = 'main'),
    path (r'^search/', views.search_results, name='search_results'),
]

#serve uploaded images on the development server 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)