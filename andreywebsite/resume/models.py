from django.db import models

# Activity and its children

class Activity(models.Model):
	def __str__(self):
		return self.name

	pub_date = models.DateTimeField('date published')

	name = models.CharField(max_length = 200)
	secName = models.CharField(max_length = 200)
	# TO DO: make this an enum or something
	# for now just char field - "Coop Work Experience", "Technical Project", "Volunteer Experience", "Education", "Professional Affiliation"
	activityType = models.CharField(max_length = 200)

	start_date = models.DateField('date activity started')
	end_date = models.DateField('date activity ended')
	
	attachments = models.CharField(max_length = 200)


class ActivityDetail(models.Model):
	def __str__(self):
		return self.detail

	pub_date = models.DateTimeField('date published', null=True)
	detail = models.CharField(max_length = 200)
	activity = models.ForeignKey(Activity, on_delete=models.CASCADE)


# Other Models
class SkillType(models.Model):
	def __str__(self):
		return self.name

	pub_date = models.DateTimeField('date published')
	name = models.CharField(max_length = 200)

class Skill(models.Model):
	def __str__(self):
		return self.name

	pub_date = models.DateTimeField('date published')

	name = models.CharField(max_length = 200)
	detail = models.ManyToManyField(Activity)
	skillType = models.ForeignKey(SkillType, on_delete=models.DO_NOTHING) 

class Interest(models.Model):
	def __str__(self):
		return self.name

	pub_date = models.DateTimeField('date published')

	name = models.CharField(max_length = 200)
	detail = models.ManyToManyField(Activity)