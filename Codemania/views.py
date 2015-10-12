from django.shortcuts import render

from django.http import HttpResponse

from .models import Problem

from django.template import RequestContext, loader

def index(request):
	problems = Problem.objects.order_by('added_at')
	template = loader.get_template('Codemania/index.html')
	context = RequestContext(request, {'problems':problems,})
	return HttpResponse(template.render(context))

