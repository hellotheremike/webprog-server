from django.http import HttpResponse

def index(request):
	try:
		f = open('visitors.txt', 'r+')
	except:
		f = open('visitors.txt', 'w+')
	
	if(f.read() == ''):
		f = open('visitors.txt', 'w+')
		f.write('0')
		num = 0
	else:
		f = open('visitors.txt', 'r+')
		num = f.read()
		num = int(num)+1
		f = open('visitors.txt', 'w+')
		f.write(str(num))
	return HttpResponse(num)