from django.db import models
from django.contrib.auth.models import User    #علشان اقدر اتعامل مع اليوزر بتاع django
# Create your models here.


class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_user')
    title=models.CharField(max_length=100)
    contnent=models.TextField(max_length=5000,verbose_name='contant')
    active=models.BooleanField(default=False)
    image=models.ImageField(upload_to='posts/',null=True,blank=True)
    file=models.FileField(upload_to='Posts/',null=True,blank=True)



    def __str__(self):
        return self.title