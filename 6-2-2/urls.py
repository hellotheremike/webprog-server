from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#Mainpage
    url(r'^$', ('app.views.index'), name="Start"),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		    url(r'^site_media/(?P<path>.*)/$',  'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	
	)
