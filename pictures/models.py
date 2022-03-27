from django.db import models

# Create your models here.
class Galore(models.Model):
    title = models.CharField(max_length=60)
    image_pic = models.ImageField(upload_to = 'photos/', null=True)
    description = models.TextField()
    # location = models.ManyToManyField(location)
    # category = models.ManyToManyField(category)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save_galleria(self):
        self.save()
    def delete_galleria(self):
        self.delete()

    # @classmethod
    # def days_post(cls,date):
    #     post = cls.objects.filter(pub_date__date = date)
    #     return post

class location(models.Model):
    locate = models.CharField(max_length =30)
    def __str__(self):
        return self.locate
    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()