from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#Mainpage
    url(r'^$', ('blog.views.index'), name="Start")
)
