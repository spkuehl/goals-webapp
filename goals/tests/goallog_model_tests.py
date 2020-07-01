from django.test import TestCase
import pytest
import datetime

from django.contrib.auth.models import User
from goals.models import Goal, GoalLog


# GOAL LOG unit tests
# Create GoalLog
@pytest.mark.django_db
def test_create_goallg(django_user_model):
    user = django_user_model.objects.create(
        username='someone', password='password'
        )
    name = 'Creative Writing'
    description = 'Write creatively 3x a week for the next 3 months.'
    end_date = datetime.datetime.now() + datetime.timedelta(days=90)

    goal_log = GoalLog(goal=goal,
                       name=name,
                       description=description,
                       end_date=end_date)
    gogoal_logal.save()
    assert len(GoalLog.objects.all()) == 1

# Edit GoalLog
# Archive GoalLog
# Add GoalLog.start_time
# Edit GoalLog.start_time
# Add GoalLog.end_time
# Edit GoalLog.end_time
# Get GoalLog duration == None if no start & end time.
# Get GoalLog duration if start & end time.
