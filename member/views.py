from django.contrib.auth.decorators import login_required
from django.core.context_processors import request
from django.views.decorators.csrf import csrf_exempt
import time
import datetime

__author__ = 'cemkiy'
__author__ = 'kaykisizcom'
__author__ = 'barisariburnu'

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from member.forms import *
from django.forms.util import ErrorList

# Create your views here.

def new_member(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/member/member_profile/')

    form = new_member_form
    if request.method == 'POST':
        form = new_member_form(request.POST)
        if form.is_valid():
            try:
                username = request.POST.get('username')
                password = request.POST.get('password')
                email = request.POST.get('email')
                member_user_auth = User.objects.create_user(username, email, password)
                member_user_auth.save()
                form.save()
                return HttpResponseRedirect('/accounts/login/')
            except Exception as e:
                print e
                return HttpResponseRedirect('/404')
    return render_to_response('new_member.html', {'form': form}, context_instance=RequestContext(request))

@login_required
def new_swap_ticket(request):
    try:
        member = Member.objects.filter(username=request.user.username)[0]
    except:
        return HttpResponseRedirect('/accounts/logout/')
    form = new_swap_ticket_form(initial={'member': member})
    if request.method == 'POST':
        form = new_swap_ticket_form(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/ticket_pool/')
            except:
                return HttpResponseRedirect('/404')
    return render_to_response('new_swap_ticket.html', locals(), context_instance=RequestContext(request))

@login_required
def member_profile(request):
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        return render_to_response('member_profile.html', locals())
    except Exception as e:
        print e
        return HttpResponseRedirect('/404')

@login_required
def edit_member_profile(request):
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        member_pw = User.objects.filter(username=request.user.username)[0]
    except Exception as e:
        print e
        return HttpResponseRedirect('/404')

    form = edit_member_profile_form()
    form_password = edit_member_password_form #for change password

    if request.method == 'POST' and 'submit' in request.POST: #normal form
        form = edit_member_profile_form(request.POST, request.FILES)
        if form.is_valid():
            try:
                member.profile_photo = request.FILES["profile_photo"]
                member.save()
                return HttpResponseRedirect('/member/member_profile')
            except Exception as e:
                print e
                return HttpResponseRedirect('/404')

    elif request.method == 'POST' and 'Change Password' in request.POST: #password form
        form_password = edit_member_password_form(request.POST)
        if form_password.is_valid():
            if member.password == request.POST.get('old_password') and request.POST.get('new_password') == request.POST.get('confirm_password'):
                try:
                    member.password = request.POST.get('new_password')
                    member_pw.set_password(request.POST.get('new_password'))
                    member.save()
                    member_pw.save()
                    return HttpResponseRedirect('/member/member_profile')
                except Exception as e:
                    print e
                    return HttpResponseRedirect('/404')
            else:
                errors = form_password._errors.setdefault("old_password", ErrorList())
                errors.append(u'Check your old and new password')

    return render_to_response('edit_member_profile.html', {'form': form, 'form_password': form_password, 'request': request}, context_instance=RequestContext(request))


def ticket_details(request, ticket_id):
    try:
        ticket = On_Sales.objects.filter(id=ticket_id)[0]
        return render_to_response('ticket_details.html', locals())
    except Exception as e:
        print e
        return HttpResponseRedirect('/404')

@login_required
def comes_shipping(request): #user own exchanges
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        orders = Orders.objects.filter(ship_to_user=member).all()
        return render_to_response('comes_shipping.html', locals())
    except Exception as e:
        print e
        return HttpResponseRedirect('/404')

@login_required
def sends_shipping(request): #user 3rd person exchanges
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        orders = Orders.objects.filter(on_sales__member=member).all()
        return render_to_response('sends_shipping.html', locals())
    except Exception as e:
        print e
        return HttpResponseRedirect('/404')

def my_bag(request): #bag is basket of my take ticket
    try:
        tickets_in_my_bag = request.session['tickets_in_my_bag']
        print tickets_in_my_bag
        tickets = On_Sales.objects.filter(id__in=tickets_in_my_bag)
        return render_to_response('my_bag.html', locals())
    except Exception as e:
        print e
        return HttpResponseRedirect('/404')

@csrf_exempt
def in_the_bucket(request): # added new ticket for ticket in my bag
     try:
        if request.session.get('tickets_in_my_bag'):
            tickets_in_my_bag = request.session['tickets_in_my_bag']
            tickets_in_my_bag.append(int(request.POST.get('ticket_id')))
            request.session['tickets_in_my_bag'] = tickets_in_my_bag
        else:
            ticket_id = int(request.POST.get('ticket_id'))
            tickets_in_my_bag = [ticket_id]
            request.session['tickets_in_my_bag'] = tickets_in_my_bag
        return HttpResponse(False, content_type='application/json')
     except Exception as e:
        print e
        return HttpResponseRedirect('/404')