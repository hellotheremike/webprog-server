from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django import forms


def index(request):
	if request.method == 'POST':
		form = First(request.POST)
		if form.is_valid():
			query = ""
			for x in form.data:
				if x != 'csrfmiddlewaretoken':
					query += x + "=" +form.data[x].strip().replace(" ", "+")+"&"
			return HttpResponseRedirect('/first/?'+query)
	else:
		form = First()

	c = {'form': form, 'index': True}
	c.update(csrf(request))
	return render_to_response('start.html', c)

def first(request):
	if request.method == 'POST':
		form = Second(request.POST)
		if form.is_valid():
			query = ""
			for x in form.data:
				if x != 'csrfmiddlewaretoken':
					query += x + "=" +form.data[x].strip().replace(" ", "+")+"&"
			return HttpResponseRedirect('/second/?'+query)
	else:
		form = Second()

	c = {'form': form, 'first': True, 'parameters': request.GET}
	c.update(csrf(request))
	return render_to_response('start.html', c)

def second(request):
	req = request.GET
	value = "<pre>"
	for x in req:
		value += x + "=" + req[x] + "\n"
	value += "</pre>"
	return HttpResponse(value)

class First(forms.Form):
    Name = forms.CharField(max_length=100)

class Second(forms.Form):
    Email = forms.EmailField()