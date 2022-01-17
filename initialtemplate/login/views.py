from django.shortcuts import render
from django.http import HttpResponse, Http404
from .forms import forms
from django.template import loader
# Create your views here.

def login(request):
	if request.method == 'GET':
		form = forms.LoginForm()
		template = loader.get_template('loginForm.html')
		context = {
			'form' : form,
		}
	elif request.method == 'POST':
                template = loader.get_template('index.html')
                context = {}
	else:
		template = loader.get_template('error.html')
		context = {
			'error' : 403
		}
	return HttpResponse(template.render(context,request))
