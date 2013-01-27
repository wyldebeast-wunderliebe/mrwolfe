from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from views.index import IndexView, AdminView
from views.issue import IssueCreate, IssueEdit, IssueView, IssueAssigneeJSONEdit
from views.service import ServiceJSONCreate, ServiceJSONEdit, \
    ServiceJSONDelete
from views.sla import SLAView, SLAJSONCreate, SLAJSONEdit, SLAJSONDelete, \
    SLADelete, SLAEdit
from views.customer import CustomerJSONCreate, CustomerJSONEdit, \
    CustomerJSONDelete
from views.operator import OperatorJSONCreate, OperatorJSONEdit, \
    OperatorJSONDelete
from views.mailqueue import MailQueueJSONCreate, MailQueueJSONEdit, \
    MailQueueJSONDelete
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

                       # Service
                       #
                       url(r'^create_service_json/(?P<sla_pk>[\d]+)$', 
                           ServiceJSONCreate.as_view(),
                           name="create_service_json"),
                       url(r'^edit_service_json/(?P<pk>[\d]+)$', 
                           ServiceJSONEdit.as_view(),
                           name="edit_service_json"),
                       url(r'^delete_service_json/(?P<pk>[\d]+)$', 
                           ServiceJSONDelete.as_view(),
                           name="delete_service_json"),

                       # SLA
                       # 
                       url(r'^create_sla_json/', 
                           SLAJSONCreate.as_view(),
                           name="create_sla_json"),
                       url(r'^edit_sla_json/(?P<pk>[\d]+)$', 
                           SLAJSONEdit.as_view(),
                           name="edit_sla_json"),
                       url(r'^edit_sla/(?P<pk>[\d]+)$', 
                           SLAEdit.as_view(),
                           name="edit_sla"),
                       url(r'^view_sla/(?P<pk>[\d]+)$', 
                           SLAView.as_view(),
                           name="view_sla"),
                       url(r'^delete_sla_json/(?P<pk>[\d]+)$',
                           SLAJSONDelete.as_view(),
                           name="delete_sla_json"),
                       url(r'^delete_sla/(?P<pk>[\d]+)$',
                           SLADelete.as_view(),
                           name="delete_sla"),
                       
                       # Customer
                       #
                       url(r'^create_customer_json/', 
                           CustomerJSONCreate.as_view(),
                           name="create_customer_json"),
                       url(r'^edit_customer_json/(?P<pk>[\d]+)$', 
                           CustomerJSONEdit.as_view(),
                           name="edit_customer_json"),
                       url(r'^delete_customer_json/(?P<pk>[\d]+)$', 
                           CustomerJSONDelete.as_view(),
                           name="delete_customer_json"),

                       # Operator
                       #
                       url(r'^create_operator_json/', 
                           OperatorJSONCreate.as_view(),
                           name="create_operator_json"),
                       url(r'^edit_operator_json/(?P<pk>[\d]+)$', 
                           OperatorJSONEdit.as_view(),
                           name="edit_operator_json"),
                       url(r'^delete_operator_json/(?P<pk>[\d]+)$', 
                           OperatorJSONDelete.as_view(),
                           name="delete_operator_json"),

                       # MailQueue
                       #
                       url(r'^create_mailqueue_json/', 
                           MailQueueJSONCreate.as_view(),
                           name="create_mailqueue_json"),
                       url(r'^edit_mailqueue_json/(?P<pk>[\d]+)$', 
                           MailQueueJSONEdit.as_view(),
                           name="edit_mailqueue_json"),
                       url(r'^delete_mailqueue_json/(?P<pk>[\d]+)$', 
                           MailQueueJSONDelete.as_view(),
                           name="delete_mailqueue_json"),
)

urlpatterns += patterns('',
                        # Pattern for serving media while developing
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': settings.STATIC_ROOT}),
                        )
