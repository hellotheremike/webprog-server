from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
	#Mainpage
    url(r'^$', ('app.views.index'), name="Start"),
    url(r'^view/$', ('app.views.view'), name="view"),
    url(r'^emptySession/$', ('app.views.emptySession'), name="emptySession"),
)