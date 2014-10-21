__author__ = 'cemkiy'

from django.conf.urls import patterns, url
from member import views
import django.contrib.auth

urlpatterns = patterns('',
                    url(r'^new_member/$', 'member.views.new_member'),
                    url(r'^new_sale_ticket/$', 'member.views.new_sale_ticket'),

                       )
