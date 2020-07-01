from rest_framework import serializers

from .models import Goal


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'name', 'description', 'end_date',
                  'progeress_check', 'progeress_check_time',
                  'reminder_notification', 'reminder_notification_time',
                  'active', 'archived']
