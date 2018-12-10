from django.db import models
from django.contrib.auth.models import User

class InterventionList(models.Model):
	deployment = models.ForeignKey(User)
	value = models.CharField(max_length=300)

	def __str__(self):
		return str(self.deployment) + ":#" +str(self.pk) + self.value

	class Meta:
		verbose_name_plural = "interventions"


class InterventionUsageSurvey(models.Model):
	deployment = models.ForeignKey(User,blank=True, null=True)
	timestamp = models.DateTimeField(blank=False)
	Intervention1 = models.BooleanField(default=False)
	value1 = models.CharField(max_length=300, default='NA')
	Intervention2 = models.BooleanField(default=False)
	value2 = models.CharField(max_length=300, default='NA')
	Intervention3 = models.BooleanField(default=False)
	value3 = models.CharField(max_length=300, default='NA')
	Intervention4 = models.BooleanField(default=False)
	value4 = models.CharField(max_length=300, default='NA')

	def __str__(self):
		return str(self.deployment) + "@"  +str(self.timestamp)

class InterventionRatingSurvey(models.Model):
	deployment = models.ForeignKey(User)
	timestamp = models.DateTimeField(blank=False)
	Rating1 = models.IntegerField(default=0)
	value1 = models.CharField(max_length=300, default='NA')
	Rating2 = models.IntegerField(default=0)
	value2 = models.CharField(max_length=300, default='NA')
	Rating3 = models.IntegerField(default=0)
	value3 = models.CharField(max_length=300, default='NA')
	Rating4 = models.IntegerField(default=0)
	value4 = models.CharField(max_length=300, default='NA')

	def __str__(self):
		return str(self.deployment) + "@"  +str(self.timestamp)



