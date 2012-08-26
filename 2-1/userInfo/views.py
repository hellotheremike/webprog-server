from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	dic = request.GET
	if len(dic) > 0:
		value = "<pre>"
		for x in dic:
			value += x + " = " + dic[x]+ "\n"
		value += "</pre>"
		return HttpResponse(value)

	return render_to_response('start.html')