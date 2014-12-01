__author__ = 'cemkiy'

from django.conf.urls import patterns, url
from member import views
import django.contrib.auth

urlpatterns = patterns('',
                    url(r'^success_url/(.+)$', 'bitcoin.views.succes_url'),
                    url(r'^cancel_url/$', 'bitcoin.views.cancel_url'),
                    url(r'^payment_page/(.+)$', 'bitcoin.views.payment_page'),
                        )