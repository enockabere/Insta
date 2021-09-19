from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
# from django.conf import settings

# User = settings.AUTH_USER_MODEL

# Create your models here.

class Image(models.Model):
    image = models.ImageField(null=True,blank=False)
    description = models.TextField()
    liked = models.ManyToManyField(User,blank=True,related_name='liked')
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name='author')
    
    def __str__(self):
        return self.description
    @property
    def num_likes(self):
        return self.likes.all().count()
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike','Unlike'),
)
class Profile(models.Model):
   dp = models.ImageField(null=True,blank=True)
   bio = models.TextField(null=True,blank=True)
   user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,related_name="posts")
   def __str__(self):
       return self.bio 
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Image,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like',max_length=10)
    
    def __str__(self):
        return str(self.post)
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Image,on_delete=models.CASCADE,related_name="comments")
    content = models.TextField()
    
    def __str__(self):
        return str(self.user.username)
# class MyUserModel(AbstractBaseUser):
#     class Meta:
#         model = User
#         fields = ['username']
#     @classmethod
#     def search_by_username(cls,search_term):
#         queries = cls.objects.filter(username__icontains=search_term)
#         return queries
