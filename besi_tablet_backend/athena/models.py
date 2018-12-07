from django.db import models
from django.contrib.auth.models import User
from pyfcm import FCMNotification
import os

class NotifyType(models.Model):
    title = models.CharField(max_length=50)
    detail = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class NotifyMap(models.Model):

    class Meta:
        unique_together = ('deployment', 'nottype')

    deployment = models.ForeignKey(User)
    nottype = models.ForeignKey(NotifyType)
    usertitle = models.CharField(max_length=50)
    userdetail = models.CharField(max_length=500)


class FireID(models.Model):
    reg_id = models.CharField(max_length=255)
    deployment = models.OneToOneField(User)
    update_time = models.DateTimeField()

    def __str__(self):
        return str(self.deployment) + " | " + str(self.reg_id)


class Notification(models.Model):
    deployment = models.ForeignKey(User)
    event_time = models.DateTimeField()
    time_created = models.DateTimeField(auto_now=True)
    ack_time = models.DateTimeField(null=True)
    nottype = models.ForeignKey(NotifyType)

    def __str__(self):
        return str(self.deployment) + " | ev " + str(self.event_time)

    def get_message_tuple(self):
        title = self.nottype.title
        detail = self.nottype.detail
        try:
            alt_msg = NotifyMap.objects.get(deployment = self.deployment, nottype=self.nottype)
            title = alt_msg.usertitle
            detail = alt_msg.userdetail
        except NotifyMap.DoesNotExist:
            pass

        return (title, detail)

    def send_to_firebase(self):

        push_service = None
        try:
            push_service = FCMNotification(api_key=os.environ["FIREBASE_API_KEY"])
        except KeyError:
            print("ERROR: No Firebase API Key set")
            return

        try:
            fire_obj = FireID.objects.get(deployment= self.deployment)
            reg_id = fire_obj.reg_id

            # check for improper id
            if reg_id == 'init':
                raise FireID.DoesNotExist

            msg_title, msg_body = self.get_message_tuple()
            ret = push_service.notify_single_device(registration_id = reg_id,
                                                    message_title = msg_title,
                                                    message_body = msg_body,
                                                    sound = "default")

            print(ret)
        except FireID.DoesNotExist:
            print("ERROR: Deployment " + str(self.deployment) + " does not have a FireID")

        return



