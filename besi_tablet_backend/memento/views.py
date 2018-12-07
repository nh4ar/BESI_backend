from django.shortcuts import render
from rest_framework import generics
from memento.models import Event
from memento.serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated

class SmartEventList(generics.ListCreateAPIView):
    """
    View to list all events for the current deployment
    """

    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Event.objects.filter(deployment=self.request.user)

    def perform_create(self, serializer):
        serializer.save(deployment=self.request.user)

class EventDetailUpdate(generics.RetrieveUpdateAPIView):
    """
    View to show specific event and update it
    """

    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Event.objects.filter(deployment=self.request.user)

    #def get_serializer(self, instance=None, data=None, many=False

