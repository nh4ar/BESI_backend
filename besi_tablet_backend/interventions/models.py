from django.db import models
from django.contrib.auth.models import User

class InterventionList(models.Model):
	deployment = models.ForeignKey(User)
	value = models.CharField(max_length=300)

	def __str__(self):
		return self.value

	class Meta:
		verbose_name_plural = "interventions"



