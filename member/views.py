from django.contrib.auth.decorators import login_required

__author__ = 'cemkiy'
__author__ = 'kaykisizcom'

from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from member.forms import *

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
            except:
                return HttpResponseRedirect('/404')
    return render_to_response('new_member.html', {'form':form}, context_instance=RequestContext(request))

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
        form = new_sale_ticket_form(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/ticket_pool/')
            except:
                return HttpResponseRedirect('/404')
    return render_to_response('new_sale_ticket.html', {'form':form}, context_instance=RequestContext(request))