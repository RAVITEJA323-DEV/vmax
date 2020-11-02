from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
	texting = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE, default=None)



	def __str__(self):
		return self.texting

class Comment(models.Model):
	op_choices = {('like','like'), ('dislike','dislike')}
	post = models.ForeignKey(Post, on_delete = models.CASCADE,blank=True,null=True)
	
	content = models.TextField(max_length=200)
	opinion= models.CharField(choices=op_choices, blank=True, max_length=20)



   