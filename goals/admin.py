from django.contrib import admin
from goals.models import Goal

class GoalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Goal, GoalAdmin)
