from django.shortcuts import render

from django.http import HttpResponse

from .models import Problem

from django.template import RequestContext, loader

def index(request):
	problems = Problem.objects.order_by('added_at')
	context = RequestContext(request, {'problems':problems,})
	return render(request,"Codemania/index.html",context)
def get_problem(request, title):
	problem = Problem.objects.filter(title = title)
	#template = loader.get_template('Codemania/problems/problem.html')
	context = RequestContext(request, {'problem':problem,})
	return render(request,"Codemania/problems/problem.html",context)
