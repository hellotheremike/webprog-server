from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import datetime


def index(request):
	index = True
	expire = (60*60)*3
	time = datetime.datetime.now()
	response = render_to_response('start.html', locals())
	response.set_cookie( 'time', time.strftime("%Y-%m-%d %H:%M") , max_age=expire)
	response.set_cookie( 'name', request.META['LOGNAME'] , max_age=expire)
	return response


def view(request):
	view = True
	if request.COOKIES.has_key('time') and request.COOKIES.has_key('name'):
		time = request.COOKIES.get('time')
		name = request.COOKIES.get('name')

    
	return render_to_response('start.html', locals())
