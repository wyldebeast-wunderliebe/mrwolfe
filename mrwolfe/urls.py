from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.decorators.csrf import csrf_exempt
from views.index import IndexView, AdminView
from views.issue import IssueCreate, IssueEdit, IssueView, \
    IssueAssigneeJSONEdit, IssueHistoryView, IssueJSONClone
from views.service import ServiceJSONCreate, ServiceJSONEdit, \
    ServiceJSONDelete, ServiceJSONSetDefault
from views.rule import RuleJSONCreate, RuleJSONEdit, RuleJSONDelete
from views.sla import SLAView, SLAJSONCreate, SLAJSONEdit, SLAJSONDelete, \
    SLADelete, SLAEdit
from views.operator import OperatorJSONCreate, OperatorJSONEdit, \
    OperatorJSONDelete
from views.contact import ContactJSONCreate, ContactJSONEdit, \
    ContactJSONDelete
from views.comment import CommentJSONCreate
from views.mailqueue import MailQueueJSONCreate, MailQueueJSONEdit, \
    MailQueueJSONDelete
from views.status import StatusJSONCreate
from views.login import LoginView
from views.help import HelpView
from views.fileupload import UploadView
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
    (r'^config$', login_required(AdminView.as_view())),
    (r'^help$', login_required(HelpView.as_view())),
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
    url(r'^change_status/(?P<issue_pk>[\d]+)$', 
        login_required(StatusJSONCreate.as_view()),
        name="change_status"),
    url(r'^change_assignee/(?P<pk>[\d]+)$', 
        login_required(IssueAssigneeJSONEdit.as_view()),
        name="change_assignee"),
    url(r'^issue_history/(?P<pk>[\d]+)$', 
        login_required(IssueHistoryView.as_view()),
        name="issue_history"),
    url(r'^clone_issue/(?P<pk>[\d]+)$', 
        login_required(IssueJSONClone.as_view()),
        name="clone_issue"),
    
    # Service
    #
    url(r'^create_service_json/(?P<sla_pk>[\d]+)$', 
        login_required(ServiceJSONCreate.as_view()),
        name="create_service_json"),
    url(r'^edit_service_json/(?P<pk>[\d]+)$', 
        login_required(ServiceJSONEdit.as_view()),
        name="edit_service_json"),
    url(r'^delete_service_json/(?P<pk>[\d]+)$', 
                           login_required(ServiceJSONDelete.as_view()),
        name="delete_service_json"),
    url(r'^set_default_service/(?P<pk>[\d]+)$',
        login_required(ServiceJSONSetDefault.as_view()),
        name="set_default_service"),

    # Rule
    #
    url(r'^create_rule_json/(?P<sla_pk>[\d]+)$', 
        login_required(RuleJSONCreate.as_view()),
        name="create_rule_json"),
    url(r'^edit_rule_json/(?P<pk>[\d]+)$', 
        login_required(RuleJSONEdit.as_view()),
        name="edit_rule_json"),
    url(r'^delete_rule_json/(?P<pk>[\d]+)$', 
        login_required(RuleJSONDelete.as_view()),
        name="delete_rule_json"),

    # SLA
    # 
    url(r'^create_sla_json/', 
        login_required(SLAJSONCreate.as_view()),
        name="create_sla_json"),
    url(r'^edit_sla_json/(?P<pk>[\d]+)$', 
        login_required(SLAJSONEdit.as_view()),
        name="edit_sla_json"),
    url(r'^edit_sla/(?P<pk>[\d]+)$', 
        login_required(SLAEdit.as_view()),
        name="edit_sla"),
    url(r'^view_sla/(?P<pk>[\d]+)$', 
        login_required(SLAView.as_view()),
        name="view_sla"),
    url(r'^delete_sla_json/(?P<pk>[\d]+)$',
        login_required(SLAJSONDelete.as_view()),
        name="delete_sla_json"),
    url(r'^delete_sla/(?P<pk>[\d]+)$',
        login_required(SLADelete.as_view()),
        name="delete_sla"),
                       
    # Operator
    #
    url(r'^create_operator_json/', 
        login_required(OperatorJSONCreate.as_view()),
        name="create_operator_json"),
    url(r'^edit_operator_json/(?P<pk>[\d]+)$', 
        login_required(OperatorJSONEdit.as_view()),
        name="edit_operator_json"),
    url(r'^delete_operator_json/(?P<pk>[\d]+)$', 
        login_required(OperatorJSONDelete.as_view()),
        name="delete_operator_json"),

    # Contact
    #
    url(r'^create_contact_json/', 
        login_required(ContactJSONCreate.as_view()),
        name="create_contact_json"),
    url(r'^edit_contact_json/(?P<pk>[\d]+)$', 
        login_required(ContactJSONEdit.as_view()),
        name="edit_contact_json"),
    url(r'^delete_contact_json/(?P<pk>[\d]+)$', 
        login_required(ContactJSONDelete.as_view()),
        name="delete_contact_json"),
    
    # MailQueue
    #
    url(r'^create_mailqueue_json/', 
        login_required(MailQueueJSONCreate.as_view()),
        name="create_mailqueue_json"),
    url(r'^edit_mailqueue_json/(?P<pk>[\d]+)$', 
        login_required(MailQueueJSONEdit.as_view()),
        name="edit_mailqueue_json"),
    url(r'^delete_mailqueue_json/(?P<pk>[\d]+)$', 
        login_required(MailQueueJSONDelete.as_view()),
        name="delete_mailqueue_json"),

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
    url(r'^create_comment/(?P<issue_pk>[\d]+)$', 
        login_required(CommentJSONCreate.as_view()),
        name="create_comment_json"),

    # Pattern for serving media while developing
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.STATIC_ROOT}),
    )
