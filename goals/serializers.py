from rest_framework import serializers

from .models import Goal, GoalLog


class GoalSerializer(serializers.ModelSerializer):
    total_duration_complete = serializers.SerializerMethodField()

    def get_total_duration_complete(self, obj):
        logs = GoalLog.objects.filter(goal=obj)
        total_hours_list = [log.duration_complete for log in logs]
        return sum(total_hours_list)

    class Meta:
        model = Goal
        fields = ['id', 'name', 'duration', 'description', 'end_date',
                  'progeress_check', 'progeress_check_time',
                  'reminder_notification', 'reminder_notification_time',
                  'active', 'archived', 'total_duration_complete']


class GoalLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalLog
        fields = ['id', 'goal', 'notes', 'start_time', 'end_time',
                  'duration_direct_input']
