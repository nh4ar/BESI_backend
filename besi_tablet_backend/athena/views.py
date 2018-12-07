from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from athena.models import Notification, NotifyType, FireID
from athena.serializers import NotificationSerializer, NotifyTypeSerializer, FireIDSerializer
from django.utils.timezone import now

class SmartNotificationList(generics.ListCreateAPIView):
    """
    View to list all notifications for the current deployment
    """

    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Notification.objects.filter(deployment=self.request.user)

    def perform_create(self, serializer):
        new_notification = serializer.save(deployment=self.request.user)
        new_notification.send_to_firebase()


class NotifyTypeList(generics.ListAPIView):
    """
    View to list all notify types
    """
    queryset = NotifyType.objects.all()
    serializer_class = NotifyTypeSerializer
    permission_classes = (IsAuthenticated, )

class FireIDUpdate(generics.RetrieveUpdateAPIView):
    """
    View to update FireIDs
    """

    serializer_class = FireIDSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        """
        Get the fire id object.
        If one does not exist for the deployment one will be created
        """
        fire_obj = None
        try:
            fire_obj = FireID.objects.get(deployment=self.request.user)
        except FireID.DoesNotExist:
            fire_obj = FireID.objects.create(deployment=self.request.user, reg_id="init", update_time=now())
            fire_obj.save()

        return fire_obj

    def perform_update(self, serializer):
        """
        When the object is updated change the time
        """
        serializer.save(update_time=now())



