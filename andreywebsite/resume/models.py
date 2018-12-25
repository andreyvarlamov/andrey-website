from django.db import models

# Activity and its children

class Activity(models.Model):
	def __str__(self):
		return self.name

	pub_date = models.DateTimeField(
		'date published', 
		auto_now_add=True, 
		)
	name = models.CharField(max_length=50)
	ACTIVITY_TYPE_CHOICES = (
		('COOPW', 'Co-op Work Experience'),
		('TECPR', 'Technical Project'),
		('VOLUX', 'Volunteer Experience'),
		('PROAF', 'Professional Affillation'),
		)
	activity_type = models.CharField(
		max_length=5,
		choices=ACTIVITY_TYPE_CHOICES,
		default='COOPW',
		)
	position = models.CharField(
		max_length=50,
		null=True,
		blank=True,
		)
	location = models.CharField(
		max_length=50,
		null=True,
		blank=True,
		)
	start_end_date = models.CharField(
		'activity start and end dates',
		max_length=50,
		null=True,
		blank=True,
		)
	attachments = models.CharField(
		max_length=50,
		null=True,
		blank=True,
		)


class ActivityDetail(models.Model):
	def __str__(self):
		return self.detail[:20]

	pub_date = models.DateTimeField(
		'date published', 
		auto_now_add=True, 
		)
	detail = models.CharField(max_length=300)
	activity = models.ForeignKey(
		Activity, 
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		)

# Other Models
class SkillType(models.Model):
	def __str__(self):
		return self.name

	name = models.CharField(max_length=50)

class Skill(models.Model):
	def __str__(self):
		return self.name

	pub_date = models.DateTimeField(
		'date published',
		auto_now_add=True,
		)
	name = models.CharField(max_length=50)
	detail = models.ManyToManyField(Activity)
	skill_type = models.ForeignKey(
		SkillType,
	 	on_delete=models.DO_NOTHING,
	 ) 

class Interest(models.Model):
	def __str__(self):
		return self.name

	pub_date = models.DateTimeField(
		'date published', 
		auto_now_add=True,
		)
	name = models.CharField(max_length=50)
	detail = models.ManyToManyField(Activity)