from django.db import models
from django.utils import timezone
from django.db.models.signals import *
from django.conf import settings
from django.contrib.auth.models import AbstractUser

#class Profile(AbstractUser):
#	firstName = models.CharField(max_length=200)
#	lastName = models.CharField(max_length=200)
#	introduce = models.CharField(max_length=200)
#	circle = models.CharField(max_length=200)
	
class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title

class Comment(models.Model):
    post = models.ForeignKey('groupong.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
