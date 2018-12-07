from rest_framework import serializers
from athena.models import Notification, NotifyType, FireID

class NotificationSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    deployment = serializers.ReadOnlyField(source='deployment.username')
    event_time = serializers.DateTimeField(required=True)
    time_created = serializers.DateTimeField(read_only=True)
    ack_time = serializers.DateTimeField(read_only=True)
    nottype = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=NotifyType.objects.all())

    def create(self,validated_data):
        return Notification.objects.create(**validated_data)

class NotifyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotifyType

class FireIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireID

    reg_id = serializers.CharField()
    deployment = serializers.ReadOnlyField(source='deployment.username')
    update_time = serializers.DateTimeField(read_only=True)
