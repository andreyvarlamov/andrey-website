from django.contrib import admin

from .models import Activity, ActivityDetail, Skill, SkillType, Interest

class ActivityDetailInline(admin.StackedInline):
	model=ActivityDetail
	fields=[('detail')]
	extra = 3

class ActivityAdmin(admin.ModelAdmin):
	fieldsets = [
		('Activity info:',	{'fields': ['name', 'secName', 'activityType']}),
		('Activity dates:', {'fields': ['start_date', 'end_date', 'pub_date']}),
		(None, 				{'fields': ['attachments']}),
	]
	inlines = [ActivityDetailInline]

# Register your models here.
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Skill)
admin.site.register(SkillType)
admin.site.register(Interest)