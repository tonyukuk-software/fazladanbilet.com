__author__ = 'cemkiy'
__author__ = 'barisariburnu'
__author__ = 'kaykisizcom'

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
                    url(r'^sends_shipping/$', 'member.views.sends_shipping'), #user 3rd person exchanges
                    url(r'^my_bag/$', 'member.views.my_bag'), #bag is basket of my take ticket
                    url(r'^in_the_bucket/$', 'member.views.in_the_bucket'),
                    url(r'^new_order/(.+)$', 'member.views.new_order'), #added cargo information by ship to
                        )
