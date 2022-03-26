from django.db import models

# Create your models here.
class Galleria(models.Model):
    name = models.CharField(max_length=60)
    image_pic = models.ImageField(upload_to = 'pics/', null=True)
    description = models.TextField()
    # location = models.ManyToManyField(location)
    # category = models.ManyToManyField(category)
    pub_date = models.DateTimeField(auto_now_add=True)