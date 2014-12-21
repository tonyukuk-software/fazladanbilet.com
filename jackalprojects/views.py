from django.template.loader import get_template

__author__ = 'cemkiy'
__author__ = 'barisariburnu'
__author__ = 'kaykisizcom'

from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from member.models import On_Sales, Member
from django.http import HttpResponseRedirect, HttpResponse
from forms import *
from mailgun import *


# Create your views here.


def home_page(request):
    tickets = On_Sales.objects.filter(active=True)
    categories = Category.objects.all()
    return render_to_response('home_page.html', locals(), context_instance=RequestContext(request))


def ticket_pool(request):
    tickets = On_Sales.objects.filter(active=True)
    categories = Category.objects.all()
    return render_to_response('ticket_pool.html', locals())


def contact_us(request):
    if request.method == 'POST':
        form = contact_us_form(request.POST)
        if form.is_valid():
            try:
                name = request.POST.get('name')
                email = request.POST.get('email')
                title = request.POST.get('title')
                message = request.POST.get('message')
                template = get_template("mail_contact_us.html")
                context = Context({'name': name,
                                   'email': email,
                                   'title': title,
                                   'message': message})
                content = template.render(context)
                mailgun_operator = mailgun()
                mailgun_operator.send_mail_with_html('info@fazladanbilet.com', content)
                return HttpResponseRedirect('/')
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry')
    return render_to_response('contact_us.html', locals(), context_instance=RequestContext(request))


def forgotten_password(request):
    text_for_result = ''
    form = forgotten_password_form()
    if request.method == 'POST':
        form = forgotten_password_form(request.POST)
        if form.is_valid():
            try:
                email = request.POST.get('email')
                member = Member.objects.filter(email=email)[0]
                if member:
                    template = get_template("mail_forgotten_password.html")
                    context = Context({'username': member.username,
                                       'password': member.password})
                    content = template.render(context)
                    mailgun_operator = mailgun()
                    mailgun_operator.send_mail_with_html(member.email, content)
                    text_for_result = 'We are send your password to your email. '
                else:
                    text_for_result = 'Wrong mail adress.'
                return HttpResponseRedirect('/accounts/login')
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry')
    return render_to_response('forgotten_password.html', locals(), context_instance=RequestContext(request))


def public_profile(request, user_id):
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        if not member.active:
            return HttpResponseRedirect('/')
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')
    return render_to_response('public_profile.html', locals())


def page_sorry(request):
    return render_to_response('sorry.html', locals())


def terms(request):
    return render_to_response('terms.html', locals(), context_instance=RequestContext(request))


def how_it_works(request):
    return render_to_response('how_it_works.html', locals(), context_instance=RequestContext(request))

def search(request, search_keyword):
    tickets = On_Sales.objects.filter(title__icontains=search_keyword).all()
    return render_to_response('search.html', locals(), context_instance=RequestContext(request))

def category_filter(request, category_keyword):
    categories = Category.objects.all()
    category_filter = Category.objects.filter(category_name=category_keyword)[0]
    tickets = On_Sales.objects.filter(category=category_filter).all()
    return render_to_response('category_filter.html', locals(), context_instance=RequestContext(request))