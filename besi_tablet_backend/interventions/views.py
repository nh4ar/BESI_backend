from django.shortcuts import render
from rest_framework import generics
from interventions.models import InterventionList
from interventions.serializers import InterventionSerializer
from rest_framework.permissions import IsAuthenticated

class SmartInterventionList(generics.ListCreateAPIView):
    """
    View to list all activities of the current deployment
    """
    serializer_class = InterventionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return InterventionList.objects.filter(deployment=self.request.user)

    def perform_create(self, serializer):
        serializer.save(deployment=self.request.user)

