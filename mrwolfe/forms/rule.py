from django import forms
from mrwolfe.models.rule import Rule


REGEXP_HELP = """ Define a regular expression. The expression will be
'searched' in the message field (using re.search). When for example
the from field is specified as 'voodoo', any email from
'voodoo@evilempire.com', 'master@voodoo.org', etc. will match.

"""


class RuleForm(forms.ModelForm):

    class Meta:
        model = Rule
        widgets = {'sla': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(RuleForm, self).__init__(*args, **kwargs)

        self.fields["regexp"].help_text = REGEXP_HELP
