from django.contrib import admin

from .models import Activity, Skill, SkillType, Interest

# Register your models here.
admin.site.register(Activity)
admin.site.register(Skill)
admin.site.register(SkillType)
admin.site.register(Interest)