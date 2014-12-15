__author__ = 'cemkiy'
__author__ = 'kaykisizcom'
__author__ = 'barisariburnu'

from django.shortcuts import render, render_to_response
from django.template import RequestContext

import requests

class mailgun:
    def __init__(self):
        self.key = 'key-2361ddc59bfd7a45df0acdac47b84390'
        self.sandbox = 'sandboxe1e55da3f7a7423ba6d16a58c3ffbee8.mailgun.org'
        self.recipient = 'info@fazladanbilet.com'

    def send_mail(self, email_to):
        request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(self.sandbox)
        request = requests.post(request_url, auth=('api', self.key), data={
            'from': self.recipient,
            'to': email_to,
            'subject': 'Hello',
            'text': 'Hello from Mailgun'
        })
        output = 'Status: {0}'.format(request.status_code) + 'Body:   {0}'.format(request.text)
        print output

    def send_mail_with_html(self, email_to, html, context):
        request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(self.sandbox)
        request = requests.post(request_url, auth=('api', self.key), data={
            'from': self.recipient,
            'to': email_to,
            'subject': 'Hello',
            'html': html
        })
        output = 'Status: {0}'.format(request.status_code) + 'Body:   {0}'.format(request.text)
        print output

def mail_email(request):
    return render_to_response('mail_email.html', locals(), context_instance=RequestContext(request))

def mail_base(request):
    return render_to_response('mail_base.html', locals(), context_instance=RequestContext(request))