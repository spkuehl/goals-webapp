from django.test import TestCase
import pytest
import datetime

from django.contrib.auth.models import User
from goals.models import Goal, GoalLog


# GOAL LOG unit tests
@pytest.mark.django_db
def test_create_goallog(django_user_model):
    user = django_user_model.objects.create(
        username='someone', password='password'
        )
    name = 'Creative Writing'
    description = 'Write creatively 3x a week for the next 3 months.'
    end_date = datetime.datetime.now() + datetime.timedelta(days=90)
    goal = Goal(user=user,
                name=name,
                description=description,
                end_date=end_date)
    goal.save()

    start_time = datetime.datetime.now()
    end_time = datetime.datetime.now() + datetime.timedelta(hours=2)
    goal_log = GoalLog(goal=goal,
                       notes='some notes on how the log went.',
                       start_time=start_time,
                       end_time=end_time)
    goal_log.save()
    assert len(GoalLog.objects.all()) == 1

# Archive GoalLog
# Add GoalLog.start_time
# Edit GoalLog.start_time
# Add GoalLog.end_time
# Edit GoalLog.end_time
# Add direct input
# Edit direct input
# Get GoalLog duration == None if no start & end time.
# Get GoalLog duration if start & end time.
# Get GoalLog duration from direct input
