from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^/$', views.home),
	url(r'^/submissions/$',views.getSubmissions),
    url(r'^/problems/$', views.index,name ='index'),
    url(r'^/problems/tags/(?P<title>[a-zA-Z0-9_.-]+)/$', views.get_problem),
    url(r'^/problems/submit',views.sendSubmission),
]

