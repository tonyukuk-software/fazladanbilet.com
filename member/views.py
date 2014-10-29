from django.contrib.auth.decorators import login_required

__author__ = 'cemkiy'
__author__ = 'kaykisizcom'

from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from member.forms import *
from django.forms.util import ErrorList

# Create your views here.

def new_member(request):
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
                form.password = password
                form.save()
                return HttpResponseRedirect('/accounts/login/')
            except Exception as e:
                print e
                return HttpResponseRedirect('/404')
    return render_to_response('new_member.html', {'form': form}, context_instance=RequestContext(request))

@login_required
def new_sale_ticket(request):
    try:
        member = Member.objects.filter(username=request.user.username)[0]
    except:
        return HttpResponseRedirect('/accounts/logout/')
    form = new_sale_ticket_form(initial={
      'member':member
    })
    if request.method == 'POST':
        form = new_sale_ticket_form(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/ticket_pool/')
            except:
                return HttpResponseRedirect('/404')
    return render_to_response('new_sale_ticket.html', {'form': form}, context_instance=RequestContext(request))

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

    elif request.method == 'POST' and 'change_password' in request.POST: #password form
        form_password = edit_member_password_form(request.POST)
        if form_password.is_valid():
            if member.password == request.POST.get('old_password') and request.POST.get('new_password') == request.POST.get('confirm_password'):
                try:
                    member.password = request.POST.get('new_password')
                    member.save()
                    return HttpResponseRedirect('/member/member_profile')
                except Exception as e:
                    print e
                    return HttpResponseRedirect('/404')
            else:
                errors = form_password._errors.setdefault("old_password", ErrorList())
                errors.append(u'Check your old and new password')

    return render_to_response('edit_member_profile.html', {'form': form, 'form_password': form_password}, context_instance=RequestContext(request))

@login_required
def ticket_details(request, ticket_id):
    try:
        ticket = On_Sales.objects.filter(id=ticket_id)[0]
        return render_to_response('ticket_details.html', locals())
    except Exception as e:
        print e
        return HttpResponseRedirect('/404')