from django.db import models

# Activity and its children

class Activity(models.Model):
	pub_date = models.DateTimeField('date published')
	#start_date = models.DateField('date activity started')
	#end_date = models.DateField('date activity ended')
	name = models.CharField(max_length = 200)
	#details = models.CharField(max_length = 200)
	attachments = models.CharField(max_length = 200)

class CoopActivity(Activity):
	pass

class TechnicalProjectActivity(Activity):
	pass

class VolunteerWorkActivity(Activity):
	pass

class EducationActivity(Activity):
	pass

class AffiliationActivity(Activity):
	pass


# Other Models

class Skill(models.Model):
	pass

class Interest(models.Model):
	pass