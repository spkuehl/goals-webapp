from django.db import models
from django.contrib.auth.models import User


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    duration = models.PositiveIntegerField(null=True, blank=True,
                      help_text='Total Goal duration in hours.')
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
    archived = models.BooleanField(default=False)

    @property
    def total_duration_complete(self):
        logs = GoalLog.objects.filter(goal=self)
        total_hours_list = [log.duration_complete for log in logs]
        return sum(total_hours_list)

    @property
    def deactivate(self):
        self.active = False
        self.save()

    @property
    def activate(self):
        self.active = True
        self.save()

    @property
    def archive(self):
        self.archived = True
        self.save()

    def __str__(self):
        return '%s: %s' % (self.user, self.name)


class GoalLog(models.Model):
    '''
    todo: Test duration method.
          Ensure GoalLog is only made by Goal owner.
          See about validating end_time > start_time.
          Find interaction when time and direct input methods exist.
    '''
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    notes =models.TextField(blank=True, null=True)
    start_time  = models.DateTimeField(null=True, blank=True)
    end_time  = models.DateTimeField(null=True, blank=True)
    duration_direct_input = models.PositiveIntegerField(null=True, blank=True,
        help_text='Direclty input duration in minutes.')

    @property
    def duration_complete(self):
        if self.duration_direct_input:
            return self.duration_direct_input
        elif self.start_time and self.end_time:
            dur = self.end_time - self.start_time
            return (dur.total_seconds() % 3600) // 60
        else:
            return None

    def __str__(self):
        return '%s: %s' % (self.goal.user, self.goal.name)
