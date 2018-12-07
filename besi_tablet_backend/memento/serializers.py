from rest_framework import serializers
from memento.models import Event

class EventSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    deployment = serializers.ReadOnlyField(source='deployment.username')
    datetime = serializers.DateTimeField(required = True)
    unread = serializers.BooleanField(required = True)

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.unread = validated_data.get('unread', instance.unread)
        instance.save()
        return instance

