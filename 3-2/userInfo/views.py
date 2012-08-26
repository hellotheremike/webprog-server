from django.shortcuts import render_to_response

def index(request):
	meta = request.META
	return render_to_response('start.html', locals())