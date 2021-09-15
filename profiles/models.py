from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   dp = models.ImageField(null=True,blank=True)
   bio = models.TextField(null=True,blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE )
   
   def __str__(self):
       return self.bio 
class Image(models.Model):
    image = models.ImageField(null=False,blank=False)
    description = models.TextField()
    comment = models.TextField(null=True,blank=True)
    likes = models.IntegerField(null=True,blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(User)
    
    def __str__(self):
        return self.description

    
