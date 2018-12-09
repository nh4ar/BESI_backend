from django.contrib import admin
from survey.models import Activity, SleepSubsurvey, EmotionSubsurvey, CaregiverEmotionSubsurvey, ObservationSubsurvey, NotificationSubsurvey, AgitationSurvey, CaregiverDailySurvey, ActivityBundle, ActivityBundleMember


class AgitationSurveyAdmin(admin.ModelAdmin):
    list_display = ('deployment', 'timestamp', 'agitimestamp', 'level')


class CaregiverDailySurveyAdmin(admin.ModelAdmin):
    list_display = ('deployment', 'timestamp')


class ActivityBundleMemberAdmin(admin.TabularInline):
    model = ActivityBundleMember
    list_display = ('activity', 'bundle')


class ActivityBundleAdmin(admin.ModelAdmin):
    list_display = ('deployment', 'timestamp')
    inlines = [ActivityBundleMemberAdmin]

admin.site.register(Activity)
admin.site.register(SleepSubsurvey)
admin.site.register(EmotionSubsurvey)
admin.site.register(CaregiverEmotionSubsurvey)
admin.site.register(ObservationSubsurvey)
admin.site.register(NotificationSubsurvey)
admin.site.register(AgitationSurvey, AgitationSurveyAdmin)
admin.site.register(ActivityBundle, ActivityBundleAdmin)
admin.site.register(CaregiverDailySurvey, CaregiverDailySurveyAdmin)
# admin.site.register(Intervention)
