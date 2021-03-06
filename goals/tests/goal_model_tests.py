from django.test import TestCase
import pytest
import datetime

from django.contrib.auth.models import User
from goals.models import Goal, GoalLog

# Test User Model
@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
  assert User.objects.count() == 1

# GOAL unit tests
@pytest.mark.django_db
def test_create_goal(django_user_model):
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
def test_deactivate_goal(django_user_model):
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
def test_reactivate_goal(django_user_model):
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

@pytest.mark.django_db
def test_archive_goal(django_user_model):
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
    goal.archive
    assert Goal.objects.first().archived == True



# Get total duration (hours worked)
