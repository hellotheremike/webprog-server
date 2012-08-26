from django.db import models
from django.contrib import admin

class Log(models.Model):
	remote_addr = models.CharField(max_length=120)
	name = models.CharField(max_length=120)
	date = models.DateTimeField(auto_now = True)
	http_user_agent = models.TextField()
