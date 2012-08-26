
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django import forms

class UploadFileForm(forms.Form):
    file  = forms.FileField()

def index(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        file_in = form.cleaned_data['file']
        size = file_in.size
        fileType = form.cleaned_data['file'].content_type;
        
        if fileType.split("/")[1] == 'png':
            handle_uploaded_file(file_in, fileType.split("/")[1])
            return HttpResponse('<img src="/site_media/file.png">')
        if fileType.split("/")[1] == 'jpeg':
            handle_uploaded_file(file_in, fileType.split("/")[1])
            return HttpResponse('<img src="/site_media/file.jpeg">')
        if fileType.split("/")[1] == 'gif':
            handle_uploaded_file(file_in, fileType.split("/")[1])
            return HttpResponse('<img src="/site_media/file.gif">')
        elif fileType.split("/")[1] == 'plain':
            return HttpResponse(file_in.read())

        value = "<pre>Mime-Type = " + str(fileType) + "\n" + "FileName = " + str(file_in) + "\n" + "size = " + str(size) + "</pre>"
        return HttpResponse(value)
    else:
        c = {'form': form}
        c.update(csrf(request))
        form = UploadFileForm()
        return render_to_response('start.html', c)

def handle_uploaded_file(f, type):
    with open('site_media/file.'+type, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)