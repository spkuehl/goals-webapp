from django.contrib import admin
from goals.models import Goal, GoalLog


class GoalAdmin(admin.ModelAdmin):
    pass


class GoalLogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Goal, GoalAdmin)
admin.site.register(GoalLog, GoalLogAdmin)
