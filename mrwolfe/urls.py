from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from views.index import IndexView, AdminView
from views.issue import IssueCreate, IssueEdit, IssueView, IssueAssigneeJSONEdit
from views.service import ServiceCreate, ServiceJSONCreate, ServiceJSONEdit, \
    ServiceJSONDelete
from views.sla import SLACreate, SLAEdit, SLAView, SLADelete
from views.customer import CustomerCreate, CustomerEdit
from views.operator import OperatorCreate
from views.mailqueue import MailQueueCreate
from views.status import StatusJSONCreate


admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', login_required(IndexView.as_view())),
                       (r'^config$', login_required(AdminView.as_view())),
                       (r'^(new/)?openid/', include('django_openid_auth.urls')),
                       (r'^logout/$', 'django.contrib.auth.views.logout'),
                       (r'^admin/', include(admin.site.urls)),
                       url(r'^create_issue/', 
                           IssueCreate.as_view(),
                           name="create_issue"),
                       url(r'^edit_issue/(?P<pk>[\d]+)$', 
                           IssueEdit.as_view(),
                           name="edit_issue"),
                       url(r'^view_issue/(?P<pk>[\d]+)$', 
                           IssueView.as_view(),
                           name="view_issue"),
                       url(r'^change_status/(?P<issue_pk>[\d]+)$', 
                           StatusJSONCreate.as_view(),
                           name="change_status/"),
                       url(r'^change_assignee/(?P<pk>[\d]+)$', 
                           IssueAssigneeJSONEdit.as_view(),
                           name="change_assignee"),
                       url(r'^create_service/', 
                           ServiceCreate.as_view(),
                           name="create_service"),
                       url(r'^create_service_json/(?P<sla_pk>[\d]+)$', 
                           ServiceJSONCreate.as_view(),
                           name="create_service_json"),
                       url(r'^edit_service_json/(?P<pk>[\d]+)$', 
                           ServiceJSONEdit.as_view(),
                           name="edit_service_json"),
                       url(r'^delete_service_json/(?P<pk>[\d]+)$', 
                           ServiceJSONDelete.as_view(),
                           name="delete_service_json"),
                       url(r'^create_sla/', 
                           SLACreate.as_view(),
                           name="create_sla"),
                       url(r'^edit_sla/(?P<pk>[\d]+)$', 
                           SLAEdit.as_view(),
                           name="edit_sla"),
                       url(r'^view_sla/(?P<pk>[\d]+)$', 
                           SLAView.as_view(),
                           name="view_sla"),
                       url(r'^delete_sla/(?P<pk>[\d]+)$',
                           SLADelete.as_view(),
                           name="delete_sla"),
                       url(r'^create_customer/', 
                           CustomerCreate.as_view(),
                           name="create_customer"),
                       url(r'^create_operator/', 
                           OperatorCreate.as_view(),
                           name="create_operator"),
                       url(r'^create_mailqueue/', 
                           MailQueueCreate.as_view(),
                           name="create_mailqueue"),
)

urlpatterns += patterns('',
                        # Pattern for serving media while developing
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': settings.STATIC_ROOT}),
                        )
