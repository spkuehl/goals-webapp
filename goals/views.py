from .models import Goal, GoalLog
from .serializers import GoalSerializer, GoalLogSerializer
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

# Get Goals for User and Gaols.total_duration_complet


class GoalViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Goal.objects.filter(archived=False)
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GoalLogViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = GoalLog.objects.all()
    serializer_class = GoalLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return GoalLog.objects.filter(goal__user=self.request.user)
