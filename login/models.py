from django.db import models
from django.contrib.auth.models import User as djangoAuthUser

# Create your models here.
class User(models.Model):
	djangoUser = models.OneToOneField(djangoAuthUser,null=True,on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
	user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL) #post will not be deleted when a user's account is removed
	title = models.CharField(max_length=200,null=True)
	content = models.TextField(max_length=500,null=True)
	date_posted = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
	user= models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
	post= models.ForeignKey(Post,null=True,on_delete=models.SET_NULL)
	content = models.TextField(max_length=500,null=True)
	date_posted = models.DateTimeField(auto_now_add=True)