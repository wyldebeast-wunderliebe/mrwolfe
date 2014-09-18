from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.decorators.csrf import csrf_exempt
from views.index import IndexView, AdminView
from views.issue import IssueCreate, IssueEdit, IssueView, \
    UpdateIssueAssignee, IssueHistoryView, IssueClone, DeleteIssue
from views.service import CreateService, UpdateService, DeleteService, \
    ServiceSetDefault
from views.rule import CreateRule, UpdateRule, DeleteRule
from views.sla import SLAView, CreateSLA, UpdateSLA, DeleteSLA
from views.operator import CreateOperator, UpdateOperator, DeleteOperator
from views.contact import CreateContact, UpdateContact, DeleteContact
from views.comment import CreateComment
from views.mailqueue import CreateMailQueue, UpdateMailQueue, DeleteMailQueue
from views.itconnector import CreateITConnector, UpdateITConnector, \
    DeleteITConnector
from views.status import CreateStatus
from views.login import LoginView
from views.help import HelpView
from views.setting import UpdateSetting
from views.fileupload import UploadView
from views.schedule import ScheduleIssue
from haystack.views import SearchView
from forms.search import SearchForm
from models import Attachment


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r"^login/*",
        LoginView.as_view(),
        name="login"),

    (r'^logout/$', 'django.contrib.auth.views.logout'),

    (r'^$', login_required(IndexView.as_view())),
    url(r'^config$', login_required(AdminView.as_view()), name="config"),

    (r'^help$', login_required(HelpView.as_view())),
    (r'^[a-zA-Z0-9]*\.md$', login_required(HelpView.as_view())),

    (r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    url(r'^search/',
        SearchView(
            form_class=SearchForm
            ), name='search'),

    # Issue
    #
    url(r'^create_issue/',
        login_required(IssueCreate.as_view()),
        name="create_issue"),
    url(r'^edit_issue/(?P<pk>[\d]+)$',
        login_required(IssueEdit.as_view()),
        name="edit_issue"),
    url(r'^view_issue/(?P<pk>[\d]+)$',
        login_required(IssueView.as_view()),
        name="view_issue"),
    url(r'^change_status/(?P<pk>[\d]+)$',
        login_required(CreateStatus.as_view()),
        name="change_status"),
    url(r'^change_assignee/(?P<pk>[\d]+)$',
        login_required(UpdateIssueAssignee.as_view()),
        name="change_assignee"),
    url(r'^issue_history/(?P<pk>[\d]+)$',
        login_required(IssueHistoryView.as_view()),
        name="issue_history"),
    url(r'^clone_issue/(?P<pk>[\d]+)$',
        login_required(IssueClone.as_view()),
        name="clone_issue"),
    url(r'^delete_issue/(?P<pk>[\d]+)$',
        login_required(DeleteIssue.as_view()),
        name="delete_issue"),
    url(r'^schedule_issue/(?P<pk>[\d]+)$',
        login_required(ScheduleIssue.as_view()),
        name="schedule_issue"),

    # Service
    #
    url(r'^create_service/(?P<sla_pk>[\d]+)$',
        login_required(CreateService.as_view()),
        name="create_service"),
    url(r'^edit_service/(?P<pk>[\d]+)$',
        login_required(UpdateService.as_view()),
        name="edit_service"),
    url(r'^delete_service/(?P<pk>[\d]+)$',
        login_required(DeleteService.as_view()),
        name="delete_service"),
    url(r'^set_default_service/(?P<pk>[\d]+)$',
        login_required(ServiceSetDefault.as_view()),
        name="set_default_service"),

    # Rule
    #
    url(r'^create_rule/(?P<sla_pk>[\d]+)$',
        login_required(CreateRule.as_view()),
        name="create_rule"),
    url(r'^edit_rule/(?P<pk>[\d]+)$',
        login_required(UpdateRule.as_view()),
        name="edit_rule"),
    url(r'^delete_rule/(?P<pk>[\d]+)$',
        login_required(DeleteRule.as_view()),
        name="delete_rule"),

    # SLA
    #
    url(r'^create_sla/',
        login_required(CreateSLA.as_view()),
        name="create_sla"),
    url(r'^edit_sla/(?P<pk>[\d]+)$',
        login_required(UpdateSLA.as_view()),
        name="edit_sla"),
    url(r'^view_sla/(?P<pk>[\d]+)$',
        login_required(SLAView.as_view()),
        name="view_sla"),
    url(r'^delete_sla/(?P<pk>[\d]+)$',
        login_required(DeleteSLA.as_view()),
        name="delete_sla"),

    # Operator
    #
    url(r'^create_operator/',
        login_required(CreateOperator.as_view()),
        name="create_operator"),
    url(r'^edit_operator/(?P<pk>[\d]+)$',
        login_required(UpdateOperator.as_view()),
        name="edit_operator"),
    url(r'^delete_operator/(?P<pk>[\d]+)$',
        login_required(DeleteOperator.as_view()),
        name="delete_operator"),

    # Contact
    #
    url(r'^create_contact/',
        login_required(CreateContact.as_view()),
        name="create_contact"),
    url(r'^edit_contact/(?P<pk>[\d]+)$',
        login_required(UpdateContact.as_view()),
        name="edit_contact"),
    url(r'^delete_contact/(?P<pk>[\d]+)$',
        login_required(DeleteContact.as_view()),
        name="delete_contact"),

    # MailQueue
    #
    url(r'^create_mailqueue/',
        login_required(CreateMailQueue.as_view()),
        name="create_mailqueue"),
    url(r'^edit_mailqueue/(?P<pk>[\d]+)$',
        login_required(UpdateMailQueue.as_view()),
        name="edit_mailqueue"),
    url(r'^delete_mailqueue/(?P<pk>[\d]+)$',
        login_required(DeleteMailQueue.as_view()),
        name="delete_mailqueue"),

    # ITConnector
    #
    url(r'^create_itconnector/',
        login_required(CreateITConnector.as_view()),
        name="create_itconnector"),
    url(r'^edit_itconnector/(?P<pk>[\d]+)$',
        login_required(UpdateITConnector.as_view()),
        name="edit_itconnector"),
    url(r'^delete_itconnector/(?P<pk>[\d]+)$',
        login_required(DeleteITConnector.as_view()),
        name="delete_itconnector"),

    # Attachments
    url(r'^view_image/(?P<pk>[\d]+)$',
        DetailView.as_view(
            model=Attachment,
            template_name="snippets/image.html"),
        name="view_image"),

    url(r'^fileupload$',
        csrf_exempt(UploadView.as_view()),
        name='add_attachment'),

    # Comment
    #
    url(r'^create_comment$',
        login_required(CreateComment.as_view()),
        name="create_comment"),

    # Settings
    #
    url(r'^set$',
        login_required(UpdateSetting.as_view()),
        name="set"),

    url(r'^set_notification$',
        login_required(UpdateSetting.as_view(
            template_name='snippets/set_notification.html')),
        name="set_notification"),

    # Pattern for serving media while developing
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.STATIC_ROOT}),
)


# Use Open ID if available
#
if ("django_openid_auth" in settings.INSTALLED_APPS):

    urlpatterns += patterns(
        "",
        (r'^openid/', include('django_openid_auth.urls'))
    )


# Use Wiki if it's there
#
if ("wiki" in settings.INSTALLED_APPS):
    from wiki.urls import get_pattern as get_wiki_pattern
    from django_notify.urls import get_pattern as get_notify_pattern

    urlpatterns += patterns(
        '',
        (r'^notify/', get_notify_pattern()),
        (r'^wiki/', get_wiki_pattern()),
        (r'^wiki', get_wiki_pattern())
    )
