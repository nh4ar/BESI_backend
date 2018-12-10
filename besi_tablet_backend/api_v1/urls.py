from django.conf.urls import url
from survey import views as s_view
from memento import views as m_view
from athena import views as athena_view
from interventions import views as intervention_view
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    url(r'^survey/fields/smart/a/$', s_view.SmartActivityList.as_view(), name='smart-activity-list'),

    url(r'^survey/activ/smart/$',s_view.SmartActivityBundleList.as_view(), name='smart-activity-report-list'),
    url(r'^survey/activ/smart/recent/$',s_view.SmartRecentActivityBundleList.as_view(), name='smart-recent-activity-report-list'),

    url(r'^survey/activ/(?P<username>\w+)/$',s_view.ActivityBundleListForDeployment.as_view(), name='giver-activ-survey'),
    url(r'^survey/activ/(?P<username>\w+)/(?P<year>[0-9]{4})/$', s_view.ActivityBundleListForDeployment.as_view(), name='cgiver-activ-survey-yy'),
    url(r'^survey/activ/(?P<username>\w+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', s_view.ActivityBundleListForDeployment.as_view(), name='cgiver-activ-survey-yy-mm'),
    url(r'^survey/activ/(?P<username>\w+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/$', s_view.ActivityBundleListForDeployment.as_view(), name='cgiver-activ-survey-yy-mm-dd'),

    url(r'^survey/activ/memb/smart/create/$',s_view.SmartActivityBundleMemberCreate.as_view(), name='smart-activity-bundle-member-list'),

    url(r'^survey/obs/create/$',s_view.SmartObservationSubsurveyCreate.as_view(), name='smart-observation-subsurvey-create'),
    url(r'^survey/emo/create/$',s_view.SmartEmotionSubsurveyCreate.as_view(), name='smart-emotion-subsurvey-create'),
    url(r'^survey/slp/create/$',s_view.SmartSleepSubsurveyCreate.as_view(), name='smart-sleep-subsurvey-create'),

    url(r'^survey/care-emo/create/',s_view.SmartCaregiverEmotionSubsurveyCreate.as_view(), name='smart-caregiver-emotion-subsurvey-create'),

    url(r'^survey/notif/create/$', s_view.SmartNotificationSubsurveyCreate.as_view(), name='smart-notification-subsurvey-create'),

    url(r'^survey/agi/smart/$', s_view.SmartAgitationSurveyList.as_view(), name='smart-agi-survey-list'),
    url(r'^survey/agi/create/$', s_view.AgitationSurveyCreate.as_view(), name='agi-survey-create'),
    url(r'^survey/agi/(?P<username>\w+)/$', s_view.AgitationSurveyListForDeployment.as_view(), name='agi-survey-list'),
    url(r'^survey/agi/(?P<username>\w+)/(?P<year>[0-9]{4})/$', s_view.AgitationSurveyListForDeployment.as_view(), name='agi-survey-list-yy'),
    url(r'^survey/agi/(?P<username>\w+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', s_view.AgitationSurveyListForDeployment.as_view(), name='agi-survey-list-yy-mm'),
    url(r'^survey/agi/(?P<username>\w+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/$', s_view.AgitationSurveyListForDeployment.as_view(), name='agi-survey-list-yy-mm-dd'),
    url(r'^survey/agi/(?P<deployid>\d+)/d/(?P<pk>\d+)/$', s_view.AgitationSurveyDetail.as_view(), name='agi-survey-detail'),

    url(r'^survey/daily/smart/$', s_view.SmartCaregiverDailySurveyList.as_view(), name='smart-cgiver-daily-survey-list'),
    url(r'^survey/daily/create/$', s_view.CaregiverDailyCreate.as_view(), name='cgiver-daily-survey-create'),
    url(r'^survey/daily/(?P<username>\w+)/$', s_view.CaregiverDailySurveyListForDeployment.as_view(), name='cgiver-daily-survey'),
    url(r'^survey/daily/(?P<username>\w+)/(?P<year>[0-9]{4})/$', s_view.CaregiverDailySurveyListForDeployment.as_view(), name='cgiver-daily-survey-yy'),
    url(r'^survey/daily/(?P<username>\w+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', s_view.CaregiverDailySurveyListForDeployment.as_view(), name='cgiver-daily-survey-yy-mm'),
    url(r'^survey/daily/(?P<username>\w+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/$', s_view.CaregiverDailySurveyListForDeployment.as_view(), name='cgiver-daily-survey-yy-mm-dd'),

    url(r'^memento/e/smart/$', m_view.SmartEventList.as_view(), name='smart-event-list' ),
    url(r'^memento/e/(?P<pk>\d+)/$', m_view.EventDetailUpdate.as_view(), name='smart-event-list' ),

    url(r'^athena/types/$', athena_view.NotifyTypeList.as_view(), name='notify-type-list'),
    url(r'^athena/fireid/smart/$', athena_view.FireIDUpdate.as_view(), name='fire-id-update'),
    url(r'^athena/notify/smart/$', athena_view.SmartNotificationList.as_view(), name='smart-notification-list'),

    #url(r'^survey/notif/smart$', s_view.SmartAgitationSurveyList.as_view(), name='smart-notif-survey-list'),
    #url(r'^survey/notif/create/$', s_view.AgitationSurveyCreate.as_view(), name='notif-survey-create'),

    ##### INTERVENTION #####
    # url(r'^interventions/intervention/create/$', s_view.SmartInterventionList.as_view(), name='smart-intervention-list'),
    url(r'^interventions/intervention/create/$', intervention_view.SmartInterventionList.as_view(), name='smart-intervention-list'),
    url(r'^interventions/intervention-usage/create/$', intervention_view.SmartInterventionUsageSubsurveyCreate.as_view(), name='smart-intervention-usage'),
    url(r'^interventions/intervention-rating/create/$', intervention_view.SmartInterventionRatingSubsurveyCreate.as_view(), name='smart-intervention-rating')
])
