from django import forms
from txtlocal.models import InboxSMS

class InboxSMSForm(forms.ModelForm):

    class Meta:
        model = InboxSMS