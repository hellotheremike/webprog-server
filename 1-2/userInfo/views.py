from django.http import HttpResponse

def index(request):
	num = request.META
	value = "<pre>"
	for key in num:
		value += str(key)+":"+str(num[key])+"\n"
	value += "</pre>"
	return HttpResponse(value)