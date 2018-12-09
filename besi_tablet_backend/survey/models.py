from django.db import models
from django.contrib.auth.models import User


class SleepSubsurvey(models.Model):
	MultipleBathroomVisits = models.BooleanField(default=False)
	DifficultyFallingAsleep = models.BooleanField(default=False)
	BadDreams = models.BooleanField(default=False)
	WakeUpFrequently = models.BooleanField(default=False)
	WakeUpEarly = models.BooleanField(default=False)
	MoreNaps = models.BooleanField(default=False)
	RestlessOveractive = models.BooleanField(default=False)

	def __str__(self):
		return str(self.pk)


class ObservationSubsurvey(models.Model):
	Frustration = models.BooleanField(default=False)
	Ambulation = models.BooleanField(default=False)
	Touching = models.BooleanField(default=False)
	Clothing = models.BooleanField(default=False)
	Physical1 = models.BooleanField(default=False)
	Physical2 = models.BooleanField(default=False)
	OralFixation = models.BooleanField(default=False)
	Repetition = models.BooleanField(default=False)
	Vocal1 = models.BooleanField(default=False)
	Vocal2 = models.BooleanField(default=False)
	Lost = models.BooleanField(default=False)
	Withdrawn = models.BooleanField(default=False)
	#Annoying = models.BooleanField(default=False) --Removed in updated list
	Shadowing = models.BooleanField(default=False)
	Communication = models.BooleanField(default=False)

	def __str__(self):
		return str(self.pk)


class NotificationSubsurvey(models.Model):
	Question1 = models.BooleanField(default=False)
	Question2 = models.BooleanField(default=False)
	Question3 = models.BooleanField(default=False)

	def __str__(self):
		return str(self.pk)


class Activity(models.Model):
	deployment = models.ForeignKey(User)
	value = models.CharField(max_length=64)

	def __str__(self):
		return self.value

	class Meta:
		verbose_name_plural = "activities"


class CaregiverEmotionSubsurvey(models.Model):
	Isolated = models.BooleanField(default=False)
	Exhausted = models.BooleanField(default=False)
	Worried = models.BooleanField(default=False)
	Frustrated = models.BooleanField(default=False)
	Discouraged = models.BooleanField(default=False)
	Rested = models.BooleanField(default=False)
	Busy = models.BooleanField(default=False)
	HangingInThere = models.BooleanField(default=False)
	Okay = models.BooleanField(default=False)
	Calm = models.BooleanField(default=False)
	Satisfied = models.BooleanField(default=False)
	Hopeful = models.BooleanField(default=False)
	Motivated = models.BooleanField(default=False)
	Confident = models.BooleanField(default=False)
	InControl = models.BooleanField(default=False)

	def __str__(self):
		return str(self.pk)


class EmotionSubsurvey(models.Model):
	ShortTemper = models.BooleanField(default=False)
	Tearfulness = models.BooleanField(default=False)
	LackReactionToPleasantEvents = models.BooleanField(default=False)
	Worrying = models.BooleanField(default=False)
	Frightened = models.BooleanField(default=False)
	TalkLess = models.BooleanField(default=False)
	AppetiteLoss = models.BooleanField(default=False)
	LossInterestInUsualActivities = models.BooleanField(default=False)
	SadExpression = models.BooleanField(default=False)
	TroublePayingAttention = models.BooleanField(default=False)
	SlowSpeech = models.BooleanField(default=False)
	SlowReaction = models.BooleanField(default=False)
	Physical = models.BooleanField(default=False)
	AnticipationOfWorst = models.BooleanField(default=False)
	LackEnergy = models.BooleanField(default=False)
	LowSelfEsteem = models.BooleanField(default=False)
	Suicidal = models.BooleanField(default=False)

	def __str__(self):
		return str(self.pk)


class ActivityBundle(models.Model):
	deployment = models.ForeignKey(User)
	timestamp = models.DateTimeField(blank=False)
	activities = models.ManyToManyField(
		Activity,
		through='ActivityBundleMember',
		through_fields=("bundle", "activity"),
	)


class ActivityBundleMember(models.Model):
	bundle = models.ForeignKey(ActivityBundle, related_name="activity_member")
	activity = models.ForeignKey(Activity)
	deployment = models.ForeignKey(User)

	def __str__(self):
		return str(self.bundle) + ", " + str(self.activity)


class AgitationSurvey(models.Model):
	deployment = models.ForeignKey(User)
	agiloc = models.CharField(blank=False,max_length=100)
	timestamp = models.DateTimeField(blank=False)
	agitimestamp = models.DateTimeField(blank=False)
	level = models.IntegerField()
	# Level of agitation scale of 1-10
	observations = models.OneToOneField(ObservationSubsurvey)
	notifications = models.OneToOneField(NotificationSubsurvey)


class CaregiverDailySurvey(models.Model):
	deployment = models.ForeignKey(User)
	timestamp = models.DateTimeField(blank=False)
	caregiverEmotions = models.OneToOneField(CaregiverEmotionSubsurvey)
	PWDEmotions = models.OneToOneField(EmotionSubsurvey, related_name="PWDEmotionSubsurvey")
	PWDSleepEvents = models.OneToOneField(SleepSubsurvey, related_name="PWDSleepSubsurvey")

# class Intervention(models.Model):
# 	deployment = models.ForeignKey(User)
# 	value = models.CharField(max_length=300)

# 	def __str__(self):
# 		return self.value

# 	class Meta:
# 		verbose_name_plural = "interventions"