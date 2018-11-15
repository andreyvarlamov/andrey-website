from django.db import models

# Activity and its children

class Activity(models.Model):
	pub_date = models.DateTimeField('date publishesd')

	name = models.CharField(max_length = 200)
	secName = models.CharField(max_length = 200)
	# TO DO: make this an enum or something
	# for now just char field - "Coop Work Experience", "Technical Project", "Volunteer Experience", "Education", "Professional Affiliation"
	activityType = models.CharField(max_length = 200)

	start_date = models.DateField('date activity started')
	end_date = models.DateField('date activity ended')
	
	attachments = models.CharField(max_length = 200)


class ActivityDetail(models.Model):
	pub_date = models.DateTimeField('date published')
	detail = models.CharField(max_length = 200)
	activity = models.ForeignKey(Activity, on_delete=models.CASCADE)


# Other Models

class Skill(models.Model):
	pass

class Interest(models.Model):
	pass