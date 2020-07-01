from rest_framework import serializers

from .models import Goal, GoalLog


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'name', 'description', 'end_date',
                  'progeress_check', 'progeress_check_time',
                  'reminder_notification', 'reminder_notification_time',
                  'active', 'archived']


class GoalLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalLog
        fields = ['id', 'goal', 'notes', 'start_time', 'end_time',
                  'duration_direct_input']
