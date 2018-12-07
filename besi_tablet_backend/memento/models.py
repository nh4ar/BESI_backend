from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    deployment = models.ForeignKey(User)
    datetime = models.DateTimeField()
    unread = models.BooleanField(default=True)

    def __str__(self):
        return str(self.deployment) + " | " + str(self.datetime)



