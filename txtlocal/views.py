from django.views.decorators.http import require_POST
from txtlocal.forms import InboxSMSForm

@require_POST
def sms_response(request):
    print request.POST
    form = InboxSMSForm(request.POST)
    if form.is_valid():
        form.save()
