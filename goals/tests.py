from django.test import TestCase
import pytest

from django.contrib.auth.models import User

# Test User Model
@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
  assert User.objects.count() == 1

# GOAL unit tests
# Create Goal
# Edit Goal
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
