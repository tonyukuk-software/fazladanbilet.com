from django.shortcuts import render_to_response
from django.template import RequestContext
from member.models import On_Sales

__author__ = 'cemkiy'
__author__ = 'barisariburnu'
__author__ = 'kaykisizcom'

# Create your views here.


def home_page(request):
    return render_to_response('home_page.html', context_instance=RequestContext(request))

def ticket_pool(request):
    tickets = On_Sales.objects.filter(active=True)
    return render_to_response('ticket_pool.html', locals())
