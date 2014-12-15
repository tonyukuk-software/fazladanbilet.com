__author__ = 'cemkiy'
__author__ = 'barisariburnu'
__author__ = 'kaykisizcom'

from django.conf.urls import patterns, url
from mailgun import views

urlpatterns = patterns('',
                    url(r'^mail_base/$', 'mailgun.views.mail_base'),
                    url(r'^mail_email/$', 'mailgun.views.mail_email'),
)
