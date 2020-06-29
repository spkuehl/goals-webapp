from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
