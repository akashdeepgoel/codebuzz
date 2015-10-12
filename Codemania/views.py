from django.shortcuts import render

from django.http import HttpResponse

from .models import Problem,Problem_submission

from django.template import RequestContext, loader

import requests

from django.utils import timezone

def home(request):
	return render(request,"Codemania/home.html",{})

def index(request):
	problems = Problem.objects.order_by('-added_at')
	context = RequestContext(request, {'problems':problems,})
	return render(request,"Codemania/index.html",context)
def get_problem(request, title):
	problem = Problem.objects.get(title = title)
	#template = loader.get_template('Codemania/problems/problem.html')
	context = RequestContext(request, {'problem':problem,})
	return render(request,"Codemania/problems/problem.html",context)

def getSubmissions(request):
	submissions = Problem_submission.objects.order_by('-submitted_at')
	context = RequestContext(request, {'submissions':submissions,})
	return render(request,"Codemania/submissions.html",context)
def sendSubmission(request):
	code_submitted = request.POST.get("code")
	problem_title = request.POST.get("problem_name")
	submission_lang = request.POST.get("language")
	problem = Problem.objects.get(title = problem_title)
	problem_input = problem.test_cases
	problem_input = problem_input.replace(",","\n")
	RUN_URL = u'http://api.hackerearth.com/code/run/'
	CLIENT_SECRET = '46bbf357e9f07fca6321b647f1e61ba34158242c'
	source = code_submitted
	data = {
	    'client_secret': CLIENT_SECRET,
	    'async': 0,
	    'source': source,
	    'input' : problem_input,
	    'lang': submission_lang,
	    'time_limit': 5,
	    'memory_limit': 262144,
	}
	response = requests.post(RUN_URL, data=data)
	response = response.json()
	compile_status = response["compile_status"]
	if compile_status!="OK":
		form = Problem_submission()
		form.submission = code_submitted
		form.problem_title = problem_title
		form.status = compile_status
		form.running_time = "INF"
		form.submitted_by = request.POST.get("user")
		form.submitted_at = timezone.now()
		form.memory_used = "INF"
		form.save()
		problem = Problem.objects.get(title = problem_title)
		#	template = loader.get_template('Codemania/problems/problem.html')
		context = RequestContext(request, {'problem':problem,})
		return render(request,"Codemania/problems/problem.html",context)
	else:
		output_status = response["run_status"]["status"]
		form = Problem_submission()
		form.submission = code_submitted
		form.problem_title = problem_title
		form.status = output_status
		form.running_time = response["run_status"]["time_used"]
		form.submitted_by = request.POST.get("user")
		form.submitted_at = timezone.now()
		form.memory_used = response["run_status"]["memory_used"]
		form.save()
		if output_status== "AC":
			output = response["run_status"]["output_html"]
			output = output.replace("<br>",",")
			output = output[:len(output)-1]
			correct = problem.correct_answer
			if output==correct:
				return render(request,"Codemania/result.html",{"status":1})
			else:
				return render(request,"Codemania/result.html",{"status":0})
		else:
			return render(request,"Codemania/result.html",{"status":0})


		

