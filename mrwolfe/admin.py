from django.contrib import admin
from models.issue import Issue
from models.sla import SLA
from models.customer import Customer


class IssueAdmin(admin.ModelAdmin):

    pass


class SLAAdmin(admin.ModelAdmin):

    pass


class CustomerAdmin(admin.ModelAdmin):

    pass


admin.site.register(Issue, IssueAdmin)
admin.site.register(SLA, SLAAdmin)
admin.site.register(Customer, CustomerAdmin)

