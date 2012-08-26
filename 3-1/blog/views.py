
from django.shortcuts import render_to_response

def index(request):
	try:
		f = open('workfile.txt', 'r+')
	except:
		f = open('workfile.txt', 'w+')
	
	if(f.read() == ''):
		f = open('workfile.txt', 'w+')
		f.write('0')
		num = 0
	else:
		f = open('workfile.txt', 'r+')
		num = f.read()
		num = int(num)+1
		f = open('workfile.txt', 'w+')
		f.write(str(num))
	return render_to_response('start.html', locals())