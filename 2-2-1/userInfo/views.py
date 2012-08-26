from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
	req = request.GET
	if len(req) > 0:
		value = "<pre>"
		for x in req:
			value += x + " = " + req[x] + "\n"
		value += "</pre>"
		return HttpResponse(value)
		
	user =  request.META
	return render_to_response('start.html', locals())