from django.db import models
from django.contrib.auth.models import User


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    end_date = models.DateField(null=True, blank=True)

    DAILY = 'DY'
    WEEKLY = 'WY'
    MONTHLY = 'MY'
    YEARLY = 'YY'
    NOTIFICATION_INTERVALS = [
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
        (YEARLY, 'Yearly')
    ]
    progeress_check = models.CharField(
        max_length=2,
        choices=NOTIFICATION_INTERVALS,
        default=None,
        null=True,
        blank=True
    )
    progeress_check_time = models.TimeField(blank=True, null=True)

    reminder_notification = models.CharField(
        max_length=2,
        choices=NOTIFICATION_INTERVALS,
        default=None,
        null=True,
        blank=True
    )
    reminder_notification_time = models.TimeField(blank=True, null=True)

    active = models.BooleanField(default=True)
    archive = models.BooleanField(default=False)


class GoalLog(models.Model):
    '''
    todo: Test duration method.
          Ensure GoalLog is only made by Goal owner.
          See about validating end_time > start_time.
    '''
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    start_time  = models.DateTimeField(null=True, blank=True)
    end_time  = models.DateTimeField(null=True, blank=True)

    def duration(self):
        if self.start_time and self.end_time:
            dur = self.end_time - self.start_time
            return dur.hours
        else:
            return None
