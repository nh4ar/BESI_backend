from django.contrib import admin
from athena.models import Notification, NotifyType, NotifyMap, FireID

class NotificationAdmin(admin.ModelAdmin):
    pass

class NotifyMapAdmin(admin.TabularInline):
    model = NotifyMap

class NotifyTypeAdmin(admin.ModelAdmin):
    inlines = [NotifyMapAdmin]

admin.site.register(FireID)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(NotifyType, NotifyTypeAdmin)
