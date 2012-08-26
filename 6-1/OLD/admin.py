from django.contrib import admin
#Importing model objects.
from userInfo.models import Log

#Bulding a set of rules fot every model, this will affect the apperance of which data that will be shown in the admin view.
class AdminBlogPost(admin.ModelAdmin):
	list_display = ('title', 'email', 'date')	
#Linking our rule-set together with our model objects.
admin.site.register(Log)
