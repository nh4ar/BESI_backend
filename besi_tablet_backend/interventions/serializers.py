from rest_framework import serializers
from interventions.models import InterventionList

class InterventionSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    deployment = serializers.ReadOnlyField(source='deployment.username')
    value = serializers.CharField()

    def create(self, validated_data):
        return InterventionList.objects.create(**validated_data)

