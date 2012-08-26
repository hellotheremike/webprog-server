from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
	#Mainpage
    url(r'^$', ('app.views.index'), name="Start"),
    url(r'^first/$', ('app.views.first'), name="first"),
    url(r'^second/$', ('app.views.second'), name="second"),
)
