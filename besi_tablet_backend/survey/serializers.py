# Serializer file to interface Android to Django REST

from rest_framework import serializers
from survey.models import *


class SleepSubsurveySerializer(serializers.ModelSerializer):
	class Meta:
		model = SleepSubsurvey

class ObservationSubsurveySerializer(serializers.ModelSerializer):
	class Meta:
		model = ObservationSubsurvey

class NotificationSubsurveySerializer(serializers.ModelSerializer):
	class Meta:
		model = NotificationSubsurvey

class ActivitySerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	deployment = serializers.ReadOnlyField(source='deployment.username')
	value = serializers.CharField()

	def create(self, validated_data):
		return Activity.objects.create(**validated_data)


class ActivityBundleMemberSerializer(serializers.ModelSerializer):

	deployment = serializers.ReadOnlyField(source='deployment.username')
	class Meta:
		model = ActivityBundleMember


class EmotionSubsurveySerializer(serializers.ModelSerializer):

	class Meta:
		model=EmotionSubsurvey


class CaregiverEmotionSubsurveySerializer(serializers.ModelSerializer):
	class Meta:
		model=CaregiverEmotionSubsurvey


class ActivityBundleSerializer(serializers.ModelSerializer):
	deployment = serializers.ReadOnlyField(source='deployment.username')
	activities = serializers.StringRelatedField(many=True, read_only=True)
	class Meta:
		model = ActivityBundle
		fields = ('pk', 'timestamp','deployment','activities')

class AgitationSurveySerializerNested(serializers.ModelSerializer):
	notifications = NotificationSubsurveySerializer(read_only=True)
	observations = ObservationSubsurveySerializer(read_only=True)
	PWDEmotions = EmotionSubsurveySerializer(read_only=True)
	class Meta:
		model = AgitationSurvey

class AgitationSurveySerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	timestamp = serializers.DateTimeField(required=True)
	agitimestamp = serializers.DateTimeField(required=True)
	deployment = serializers.ReadOnlyField(source='deployment.username')
	level = serializers.IntegerField(required=True)
	agiloc = serializers.CharField(required=True)
	observations = serializers.PrimaryKeyRelatedField(queryset=ObservationSubsurvey.objects.all())
	notifications = serializers.PrimaryKeyRelatedField(queryset=NotificationSubsurvey.objects.all())

	def validate_level(self, value):
		"""
		Check that level is from 1-10
		"""
		if value > 10 or value < 1:
			raise serializers.ValidationError("Level is not inside correct range [1-10]")
		return value

	def create(self, validated_data):
		"""
		Create and return a new AgitationSurvey instance, given validated data
		"""
		return AgitationSurvey.objects.create(**validated_data)


class CaregiverDailySurveySerializerNested(serializers.ModelSerializer):
	caregiverEmotions = CaregiverEmotionSubsurveySerializer(read_only=True)
	PWDEmotions = EmotionSubsurveySerializer(read_only=True)
	PWDSleepEvents = SleepSubsurveySerializer(read_only=True)

	class Meta:
		model = CaregiverDailySurvey

class CaregiverDailySurveySerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	timestamp = serializers.DateTimeField(required=True)
	deployment = serializers.ReadOnlyField(source='deployment.username')
	caregiverEmotions = serializers.PrimaryKeyRelatedField(queryset=CaregiverEmotionSubsurvey.objects.all())
	PWDEmotions = serializers.PrimaryKeyRelatedField(queryset=EmotionSubsurvey.objects.all())
	PWDSleepEvents = serializers.PrimaryKeyRelatedField(queryset=SleepSubsurvey.objects.all())

	def create(self, validated_data):
		"""
		Create and return a new AgitationSurvey instance, given validated data
		"""
		return CaregiverDailySurvey.objects.create(**validated_data)

class InterventionSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	deployment = serializers.ReadOnlyField(source='deployment.username')
	value = serializers.CharField()

	def create(self, validated_data):
		return Intervention.objects.create(**validated_data)