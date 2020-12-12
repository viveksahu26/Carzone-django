from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=150)
    twitter_link = models.URLField(max_length=150)
    linked_in = models.URLField(max_length=150)
    instagram_link = models.URLField(max_length=150)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    