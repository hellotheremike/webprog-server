from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#Mainpage
    url(r'^$', ('userInfo.views.index'), name="Start"),
)

