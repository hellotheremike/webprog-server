
from django.shortcuts import render_to_response
from django.http import HttpResponse
def index(request):
	return render_to_response('start.html', locals())

def first(request):
	req = request.GET
	value = ""
	for x in req:
		data = req[x].replace(" ", "+")
		value += "Epost : <a href='/second/?" + x + "=" + data + "&mail=mickey@mail.com'>?" + x + "=" + data + "&mail=mickey@mail.com</a><br>"
		value += "Epost : <a href='/second/?" + x + "=" + data + "&mail=rumble@mail.com'>?" + x + "=" + data + "&mail=rumble@mail.com</a>"
	return HttpResponse(value)

def second(request):
	req = request.GET
	value = "<pre>"
	for x in req:
		value += x + "=" + req[x] + "\n"
	value += "</pre>"
	return HttpResponse(value)