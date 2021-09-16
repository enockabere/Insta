from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Profile(models.Model):
   dp = models.ImageField(null=True,blank=True)
   bio = models.TextField(null=True,blank=True)
   user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,related_name="posts")
   
   def __str__(self):
       return self.bio 
class Image(models.Model):
    image = models.ImageField(null=False,blank=False)
    description = models.TextField()
    comment = models.TextField(null=True,blank=True)
    likes = models.ManyToManyField(User,blank=True,related_name='likes')
    dislikes = models.ManyToManyField(User,blank=True,related_name='dislikes')
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    
    def __str__(self):
        return self.description
class MyUserModel(AbstractUser):
    @classmethod
    def search_by_username(cls,search_query):
        queries = cls.objects.filter(username__icontains=search_query)
        return queries
