from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Question,Post
from datetime import date
import datetime
# Create your views here.

class Home(TemplateView):
	template_name='home.html'

class Blog(TemplateView):
	template_name='blog.html'

	def get_context_data(self):
		qs=Post.objects.all()
		context={'object_list':qs}
		return context

class Today(TemplateView):
	template_name='today.html'

	def get_context_data(self):
		qs=Question.objects.all().filter(Date=datetime.datetime.today().date())
		context={'object_list' : qs}
		return context