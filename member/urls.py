__author__ = 'cemkiy'

from django.conf.urls import patterns, url
from member import views
import django.contrib.auth

urlpatterns = patterns('',
                    url(r'^new_member/$', 'member.views.new_member'),
                    url(r'^new_swap_ticket/$', 'member.views.new_swap_ticket'),
                    url(r'^member_profile/$', 'member.views.member_profile'),
                    url(r'^edit_member_profile/$', 'member.views.edit_member_profile'),
                    url(r'^ticket_details/(.+)$', 'member.views.ticket_details'),
                    url(r'^comes_shipping/$', 'member.views.comes_shipping'), #user own exchanges
                       )
