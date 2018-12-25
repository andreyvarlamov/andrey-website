from django.contrib import admin

from .models import Activity, ActivityDetail, Skill, SkillType, Interest

class ActivityDetailInline(admin.StackedInline):
	model=ActivityDetail
	fields=[('detail')]
	extra = 3

class ActivityAdmin(admin.ModelAdmin):
	fieldsets = [
		('ACTIVITY INFO',	{'fields': ['name', 'activity_type', 'position', 'location', 'start_end_date', 'attachments']}),
	]
	inlines = [ActivityDetailInline]

# Register your models here.
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Skill)
admin.site.register(SkillType)
admin.site.register(Interest)