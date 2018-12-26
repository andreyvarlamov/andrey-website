from django.urls import path

from . import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('activities', views.ActivityView.as_view(), name='activities'),
	]