from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.core.context_processors import csrf
from django import forms


def index(request):
	if request.session.get('User_name') == None:
		if request.method == 'POST':
			form = UserForm(request.POST)
			if form.is_valid():
				request.session['User_name'] = request.POST['Name']
				request.session['Ip'] = request.META['REMOTE_ADDR']
				return HttpResponseRedirect('/view/')
		else:
			form = UserForm()

		c = {'form': form, 'index': True}
		c.update(csrf(request))
		return render_to_response('start.html', c)
	else:
		return HttpResponseRedirect('/view/')


def view(request):
	if request.session.get('User_name') == None:
		return HttpResponse("No active sessions<br><a href='/'>Back</a>")
	req = request.session
	return render_to_response('start.html', locals())


def emptySession(request):
	try:
		del request.session['User_name']
		del request.session['Ip']
	except KeyError:
		pass
	return HttpResponseRedirect('/')

class UserForm(forms.Form):
	Name = forms.CharField(initial='Your name')
