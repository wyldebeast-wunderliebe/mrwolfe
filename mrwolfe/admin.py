from django.contrib import admin
from models.issue import Issue
from models.sla import SLA


class IssueAdmin(admin.ModelAdmin):

    pass


class SLAAdmin(admin.ModelAdmin):

    pass


admin.site.register(Issue, IssueAdmin)
admin.site.register(SLA, SLAAdmin)

