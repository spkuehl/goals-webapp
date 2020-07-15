from django.contrib import admin
from goals.models import Goal, GoalLog


class GoalLogAdmin(admin.ModelAdmin):
    pass


class GoalLogline(admin.TabularInline):
    model = GoalLog


class GoalAdmin(admin.ModelAdmin):
    inlines = [
        GoalLogline,
    ]
    pass


admin.site.register(Goal, GoalAdmin)
admin.site.register(GoalLog, GoalLogAdmin)
