__author__ = 'cemkiy'

from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext

from member.forms import *


def new_member(request):

    form = new_member_form
    if request.method == 'POST':
        form = new_member_form(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/member/accounts/login/')
            except:
                return HttpResponseRedirect('/asd')
    return render_to_response('new_member.html', {'form':form}, context_instance=RequestContext(request))