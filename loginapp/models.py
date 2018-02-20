from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userinfo(models.Model):
    user=models.OneToOneField(User ,related_name='oser',on_delete=models.CASCADE)
    profile_pic=models.FileField(upload_to = 'propic')
    firstname = models.CharField(max_length=50,null=True)
    lastname = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.firstname