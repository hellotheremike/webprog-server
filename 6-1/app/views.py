
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

#Import models objects
from app.models import Log

#Index function that retrurns a start page that contains all blogposts
def index(request):
	newLogg = Log(remote_addr=request.META["REMOTE_ADDR"], http_user_agent=request.META["HTTP_USER_AGENT"], name=request.META['LOGNAME'])
	newLogg.save()
	loggs = Log.objects.all().order_by("-date")
	return render_to_response('start.html', {'Loggs':loggs})

