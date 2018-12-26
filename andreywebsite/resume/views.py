from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import Activity, Skill, Interest

# Create your views here.

class IndexView(generic.ListView):
	template_name = "resume/index_activities.html"
	context_object_name = "all_models"
	queryset = Activity.objects.all()
	

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['skills'] = Skill.objects.all()
		context['interests'] = Interest.objects.all()
		return context

class ActivityView(generic.ListView):
	template_name = "resume/activities.html"
	context_object_name = "activities"
	queryset = Activity.objects.all()