from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Score(models.Model):
	'''Result = models.CharField(max_length=36,default = " ")
	name = models.CharField(max_length=36,default = " ") 
	lastname = models.CharField(max_length=36,default = " ")'''
	#Result = models.CharField(max_length=36,default = " ")
	Tenthmarks = models.IntegerField(default = 0)
	Twelfthmarks = models.IntegerField(default = 0)
	Gender = models.IntegerField(default = 0)
	Sports = models.IntegerField(default = 0)
	Indo = models.IntegerField(default = 0)
	Danc = models.IntegerField(default = 0)
	Teach = models.IntegerField(default = 0)
	Art = models.IntegerField(default = 0)
	Sing = models.IntegerField(default = 0)
	WestClass = models.IntegerField(default = 0)
	Fest = models.IntegerField(default = 0)
	Speech = models.IntegerField(default = 0)
	Gam = models.IntegerField(default = 0)
	Strict = models.IntegerField(default = 0)
	ClassR = models.IntegerField(default = 0)
	Oly = models.IntegerField(default = 0)
	OlyMar = models.IntegerField(default = 0)
	Ess = models.IntegerField(default = 0)
	Head = models.IntegerField(default = 0)
	

class Post(models.Model):
	title = models.CharField(max_length = 255)
	title_tag = models.CharField(max_length = 255, default = "Profession Rav.")
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	body = models.TextField()

	def __str__(self):
		return self.title + ' | ' + str(self.author)

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name = "comments", on_delete = models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return '%s - %s' % (self.post.title,self.name)


class Contact(models.Model):
	name = models.CharField(max_length=255) #decrease the max_length for blacbox testing
	contact = models.CharField(max_length=255)
	query = models.TextField()
