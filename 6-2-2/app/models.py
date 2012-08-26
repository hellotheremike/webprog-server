from django.db import models
from django.contrib import admin

class Posts(models.Model):
	url = models.URLField()
	name = models.CharField(max_length=120)
	date = models.DateTimeField(auto_now = True)
	email = models.EmailField()
	comment = models.TextField()
	image = models.FileField(upload_to='img/upload')
	imageType = models.CharField(max_length=50)

