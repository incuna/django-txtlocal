from django.db import models
from django.utils.translation import ugettext_lazy as _

class InboxSMS(models.Model):
    """
        This models saves POST parameters that txtlocal sends together with inbox SMS.
    """
    sender = models.CharField(_('The mobile number of the handset.'), max_length=20)
    content = models.CharField(_('The message content.'), max_length=255, blank=True)
    in_number = models.CharField(_('The number the message was sent to (your inbound number).'), max_length=20, blank=True)
    email = models.CharField(_('Any email address extracted.'), max_length=100, blank=True)
    credits = models.IntegerField(_('The number of credits remaining on your Txtlocal account.'), blank=True, null=True)
    time = models.DateTimeField(_('Date and time when parameters were received'), auto_now_add=True, blank=True)

    def __unicode__(self):
        return u"%s" % (self.content)

    class Meta:
        verbose_name_plural = _('Inbox SMS')
