from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions
from survey.models import *
from survey.serializers import *
from survey.permissions import OwnDeployment
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework import status
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.mixins import CreateModelMixin

class SmartEmotionSubsurveyCreate(generics.CreateAPIView):
	serializer_class = EmotionSubsurveySerializer
	permission_classes = (IsAuthenticated,)


class SmartSleepSubsurveyCreate(generics.CreateAPIView):
	serializer_class = SleepSubsurveySerializer
	permission_classes = (IsAuthenticated,)

class SmartCaregiverEmotionSubsurveyCreate(generics.CreateAPIView):
	serializer_class = CaregiverEmotionSubsurveySerializer
	permission_classes = (IsAuthenticated,)

class SmartActivityList(generics.ListCreateAPIView):
	"""
	View to list all activities of the current deployment
	"""
	serializer_class = ActivitySerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Activity.objects.filter(deployment=self.request.user)

	def perform_create(self, serializer):
		serializer.save(deployment=self.request.user)

class SmartInterventionList(generics.ListCreateAPIView):
	"""
	View to list all activities of the current deployment
	"""
	serializer_class = InterventionSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Intervention.objects.filter(deployment=self.request.user)

	def perform_create(self, serializer):
		serializer.save(deployment=self.request.user)



class SmartObservationSubsurveyCreate(generics.CreateAPIView):
	"""
	View to create new Observation Subsurveys
	"""
	serializer_class = ObservationSubsurveySerializer
	permission_classes = (IsAuthenticated,)

class SmartNotificationSubsurveyCreate(generics.CreateAPIView):
	serializer_class = NotificationSubsurveySerializer
	permission_classes = (IsAuthenticated,)

class SmartActivityBundleMemberCreate(APIView):
	"""
	View to list all ActivityBundles of the current deployment
	"""

	def post(self, request, format=None):
		serializer = ActivityBundleMemberSerializer(data=request.data, many=True)
		if serializer.is_valid():
			serializer.save(deployment=request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SmartActivityBundleList(generics.ListCreateAPIView):
	"""
	View to list all activity reports of the current deployment
	"""

	serializer_class = ActivityBundleSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return ActivityBundle.objects.filter(deployment=self.request.user)

	def perform_create(self, serializer):
		serializer.save(deployment=self.request.user)

class SmartRecentActivityBundleList(generics.ListAPIView):
	"""
	View to list all recent activities of the current deployment
	"""
	serializer_class = ActivityBundleSerializer
	permission_classes = (IsAuthenticated,)
	paginate_by = 20;

	def get_queryset(self):
		return ActivityBundle.objects.filter(deployment=self.request.user).order_by('timestamp')


class SmartAgitationSurveyList(generics.ListCreateAPIView):
	"""
	View to list all agitation surveys for the current deployment
	"""

	serializer_class = AgitationSurveySerializer
	permission_classes = (IsAuthenticated,)
	paginate_by = 10

	def get_queryset(self):
		return AgitationSurvey.objects.filter(deployment=self.request.user)

	def perform_create(self, serializer):
		serializer.save(deployment=self.request.user)


@permission_classes((IsAuthenticated, OwnDeployment))
class AgitationSurveyDetail(APIView):
	"""
	View a single Agitation survey by userid and pk
	"""

	def get(self, request, deployid, pk, format=None):
		survey = get_object_or_404(AgitationSurvey, id=pk)
		if survey.deployment.id != int(deployid):
			raise PermissionDenied
		self.check_object_permissions(self.request, survey)
		serializer = AgitationSurveySerializer(survey)
		return Response(serializer.data)


@permission_classes((IsAuthenticated,))
class AgitationSurveyCreate(APIView):
	"""
	Create a new agitation survey
	"""

	def post(self, request, format=None):
		serializer = AgitationSurveySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(deployment=request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated, ))
class AgitationSurveyListForDeployment(APIView):
	"""
	View all agitation surveys from a single deployment

	* Only admin/staff can view any -- otherwise users are disallowed access to all but own data
	"""

	def get(self, request,  username, year=None, month=None, day=None, format=None):
		#Control access
		user = get_object_or_404(User, username=username)

		if request.user != user and not request.user.is_staff:
			raise PermissionDenied

		#Get all surveys from deployment
		surveys = AgitationSurvey.objects.filter(deployment=user)
		#Filter by year then month then day
		if year:
			print(year)
			surveys = surveys.filter(timestamp__year=str(year))
		if month:
			surveys = surveys.filter(timestamp__month=str(month))
		if day:
			surveys = surveys.filter(timestamp__day=str(day))
		serializer = AgitationSurveySerializerNested(surveys, many=True)
		return Response(serializer.data)


class SmartCaregiverDailySurveyList(generics.ListCreateAPIView):
	"""
	View to list all daily surveys for the current deployment
	"""

	serializer_class = CaregiverDailySurveySerializer
	permission_classes = (IsAuthenticated,)
	paginate_by = 10

	def get_queryset(self):
		return CaregiverDailySurvey.objects.filter(deployment=self.request.user)

	def perform_create(self, serializer):
		serializer.save(deployment=self.request.user)


@permission_classes((IsAuthenticated, OwnDeployment))
class CaregiverDailySurveyDetail(APIView):

	"""
	View a single Caregiver Daily Survey by userid and pk
	"""

	def get(self, request, deployid, pk, format=None):
		survey = get_object_or_404(CaregiverDailySurvey, id=pk)
		if survey.deployment.id != int(deployid):
			print("BAD ID COMBO")
			raise PermissionDenied
		self.check_object_permissions(self.request, survey)
		serializer = CaregiverDailySurveySerializer(survey)
		return Response(serializer.data)



@permission_classes((IsAuthenticated, ))
class CaregiverDailySurveyListForDeployment(APIView):

	"""
	View all daily surveys from a single deployment

	* Only admin/staff can view any -- otherwise users are disallowed access to all but own data
	"""

	def get(self, request,  username, year=None, month=None, day=None, format=None):
		#Control access

		user = get_object_or_404(User, username=username)

		if request.user != user and not request.user.is_staff:
			raise PermissionDenied

		#Get all surveys from deployment
		surveys = CaregiverDailySurvey.objects.filter(deployment=user)
		#Filter by year then month then day
		if year:
			print(year)
			surveys = surveys.filter(timestamp__year=str(year))
		if month:
			surveys = surveys.filter(timestamp__month=str(month))
		if day:
			surveys = surveys.filter(timestamp__day=str(day))
		serializer = CaregiverDailySurveySerializerNested(surveys, many=True)
		return Response(serializer.data)


@permission_classes((IsAuthenticated,))
class CaregiverDailyCreate(APIView):
	"""
	Create a new agitation survey
	"""

	def post(self, request, format=None):
		serializer = CaregiverDailySurveySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(deployment=request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated, ))
class ActivityBundleListForDeployment(APIView):

	"""
	View all daily surveys from a single deployment

	* Only admin/staff can view any -- otherwise users are disallowed access to all but own data
	"""

	def get(self, request,  username, year=None, month=None, day=None, format=None):
		#Control access

		user = get_object_or_404(User, username=username)

		if request.user != user and not request.user.is_staff:
			raise PermissionDenied

		#Get all surveys from deployment
		bundles = ActivityBundle.objects.filter(deployment=user)
		#Filter by year then month then day
		if year:
			print(year)
			bundles = bundles.filter(timestamp__year=str(year))
		if month:
			bundles = bundles.filter(timestamp__month=str(month))
		if day:
			bundles = bundles.filter(timestamp__day=str(day))
		serializer = ActivityBundleSerializer(bundles, many=True)
		return Response(serializer.data)
