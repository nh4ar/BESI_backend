from rest_framework import serializers
from interventions.models import *

class InterventionSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    deployment = serializers.ReadOnlyField(source='deployment.username')
    value = serializers.CharField()

    def create(self, validated_data):
        return InterventionList.objects.create(**validated_data)

class InterventionUsageSurveySerializer(serializers.ModelSerializer):

	class Meta:
		model = InterventionUsageSurvey

class InterventionRatingSurveySerializer(serializers.ModelSerializer):

	class Meta:
		model = InterventionRatingSurvey
	# deployment = serializers.ReadOnlyField(source='deployment.username')
	# timestamp = serializers.DateTimeField(required=True)
	# Rating1 = serializers.IntegerField(required=True)
	# value1 = serializers.CharField(required=True)
	# Rating2 = serializers.IntegerField(required=True)
	# value2 = serializers.CharField(required=True)
	# Rating3 = serializers.IntegerField(required=True)
	# value3 = serializers.CharField(required=True)
	# Rating4 = serializers.IntegerField(required=True)
	# value4 = serializers.CharField(required=True)

	# def create(self, validated_data):
	# 	"""
	# 	Create and return a new AgitationSurvey instance, given validated data
	# 	"""
	# 	return InterventionRatingSurvey.objects.create(**validated_data)

