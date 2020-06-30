from django.test import TestCase
import pytest
import datetime

from django.contrib.auth.models import User
from .models import Goal, GoalLog

# Test User Model
@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
  assert User.objects.count() == 1

# GOAL unit tests
@pytest.mark.django_db
def test_goal_create(django_user_model):
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
    assert len(Goal.objects.all()) == 1

@pytest.mark.django_db
def test_goal_deactivate_goal(django_user_model):
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
    goal.deactivate
    assert Goal.objects.first().active == False

@pytest.mark.django_db
def test_goal_reactivate_goal(django_user_model):
    user = django_user_model.objects.create(
        username='someone', password='password'
        )
    name = 'Creative Writing'
    description = 'Write creatively 3x a week for the next 3 months.'
    end_date = datetime.datetime.now() + datetime.timedelta(days=90)

    goal = Goal(user=user,
                name=name,
                description=description,
                end_date=end_date,
                active=False)
    goal.save()
    goal.activate
    assert Goal.objects.first().active == True


# Deactivate Goal
# Archive Goal
# Get total duration (hours worked)

# GOAL LOG unit tests
# Create GoalLog
# Edit GoalLog
# Archive GoalLog
# Add GoalLog.start_time
# Edit GoalLog.start_time
# Add GoalLog.end_time
# Edit GoalLog.end_time
# Get GoalLog duration == None if no start & end time.
# Get GoalLog duration if start & end time.
