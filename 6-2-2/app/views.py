from django.shortcuts import render_to_response
from django.utils.html import strip_tags
from django.core.context_processors import csrf
from django import forms


#Import models objects
from app.models import Posts

#Index function that retrurns a start page that contains all blogposts

def index(request):
	if request.method == 'POST':
		form = CommentForm(request.POST, request.FILES)
		print form
		if form.is_valid():
			Email = strip_tags(request.POST['Email'])
			Name = strip_tags(request.POST['Name'])
			Url = strip_tags(request.POST['Url'])
			Comment = strip_tags(request.POST['Comment'])
			Image = form.cleaned_data['Image']
			print Image
			if Image.content_type.split("/")[0] == 'image':
				newComment = Posts(name=Name, email=Email, url=Url, comment=Comment, image=Image, imageType=Image.content_type)
				newComment.save()
	else:
		form = CommentForm()

	posts = Posts.objects.all().order_by("-date")
	c = {'form': form, 'Posts' : posts}
	c.update(csrf(request))
	return render_to_response('start.html', c)

class CommentForm(forms.Form):
	Email = forms.EmailField()
	Name = forms.CharField(initial='Your name')
	Url = forms.URLField(initial='http://')
	Comment = forms.CharField(widget=forms.Textarea)
	Image  = forms.FileField()


