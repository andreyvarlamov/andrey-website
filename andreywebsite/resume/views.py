from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import Activity

# Create your views here.

class IndexView(generic.ListView):
	template_name = "resume/index.html"
	context_object_name = "all_activities"
	
	def get_queryset(self):
		return Activity.objects.all()