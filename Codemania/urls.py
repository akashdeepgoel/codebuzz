from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/tags/(?P<title>[a-zA-Z0-9_.-]+)/$', views.get_problem)
]

