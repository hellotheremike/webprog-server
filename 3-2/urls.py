from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
	#Mainpage
    url(r'^$', ('userInfo.views.index'), name="Start"),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		    url(r'^site_media/(?P<path>.*)/$',  'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	
	)
