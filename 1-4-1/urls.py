from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('',
	#Mainpage
    url(r'^$', ('userInfo.views.index'), name="Start"),
    url(r'^img/$', ('userInfo.views.img'), name="Start"),
)