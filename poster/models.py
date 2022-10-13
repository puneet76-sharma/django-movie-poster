from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Poster(models.Model):
    name= models.CharField(max_length=100)
    image = models.ImageField(upload_to='%Y/%m/%d/', blank=True, null=True)
    user_fk = models.ManyToManyField(to=User, related_name='user_author')

    
    def __str__(self):
        return self.name
