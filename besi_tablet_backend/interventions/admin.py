from django.contrib import admin
from interventions.models import *

# Register your models here.
admin.site.register(InterventionList)
admin.site.register(InterventionUsageSurvey)
admin.site.register(InterventionRatingSurvey)

