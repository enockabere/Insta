from django.db import models

# Create your models here.
class Profile(models.Model):
   dp = models.ImageField(null=False,blank=False)
   bio = models.TextField()
   
   def __str__(self):
       return self.bio 
class Image(models.Model):
    image = models.ImageField(null=False,blank=False)
    description = models.TextField()
    comment = models.TextField()
    likes = models.IntegerField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description

    
