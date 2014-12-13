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
                return HttpResponseRedirect('/sorry')
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
                return HttpResponseRedirect('/sorry')
    return render_to_response('new_swap_ticket.html', locals(), context_instance=RequestContext(request))


@login_required
def member_profile(request):
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        return render_to_response('member_profile.html', locals())
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')


@login_required
def edit_member_profile(request):
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        member_pw = User.objects.filter(username=request.user.username)[0]
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')

    form = edit_member_profile_form()
    form_password = edit_member_password_form  # for change password

    if request.method == 'POST' and 'submit' in request.POST:  # normal form
        form = edit_member_profile_form(request.POST, request.FILES)
        if form.is_valid():
            try:
                member.profile_photo = request.FILES["profile_photo"]
                member.save()
                return HttpResponseRedirect('/member/member_profile')
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry')

    elif request.method == 'POST' and 'Change Password' in request.POST:  # password form
        form_password = edit_member_password_form(request.POST)
        if form_password.is_valid():
            if member.password == request.POST.get('old_password') and request.POST.get(
                    'new_password') == request.POST.get('confirm_password'):
                try:
                    member.password = request.POST.get('new_password')
                    member_pw.set_password(request.POST.get('new_password'))
                    member.save()
                    member_pw.save()
                    return HttpResponseRedirect('/member/member_profile')
                except Exception as e:
                    print e
                    return HttpResponseRedirect('/sorry')
            else:
                errors = form_password._errors.setdefault("old_password", ErrorList())
                errors.append(u'Check your old and new password')

    return render_to_response('edit_member_profile.html',
                              {'form': form, 'form_password': form_password, 'request': request},
                              context_instance=RequestContext(request))


def ticket_details(request, ticket_id):
    try:
        ticket = On_Sales.objects.filter(id=ticket_id)[0]
        return render_to_response('ticket_details.html', locals())
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')


@login_required
def comes_shipping(request):  # user own exchanges
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        orders = Orders.objects.filter(ship_to_user=member).all()
        return render_to_response('comes_shipping.html', locals())
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')


@login_required
def sends_shipping(request):  # user 3rd person exchanges
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        orders = Orders.objects.filter(on_sales__member=member).all()
        return render_to_response('sends_shipping.html', locals())
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')


@login_required
def send_cargo_no_and_user_url_for_btc_send(request, order_id):
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        order = Orders.objects.filter(id=order_id, on_sales__member=member)[0]
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')

    form = send_cargo_no_and_user_url_for_btc_send_form
    if request.method == 'POST':
        form = send_cargo_no_and_user_url_for_btc_send_form(request.POST)
        if form.is_valid():
            try:
                cargo_no = request.POST.get('cargo_no')
                user_url_for_btc_send = request.POST.get('user_url_for_btc_send')
                order.cargo_no = cargo_no
                order.user_url_for_btc_send = user_url_for_btc_send
                order.status = '3'
                order.save()
                return HttpResponseRedirect('/member/sends_shipping/')
            except:
                return HttpResponseRedirect('/sorry')

    return render_to_response('send_cargo_no_and_user_url_for_btc_send.html', locals(), context_instance=RequestContext(request))

def my_bag(request):  # bag is basket of my take ticket
    try:
        tickets_in_my_bag = request.session['tickets_in_my_bag']
        ids = []
        print tickets_in_my_bag
        for i in range(0, len(tickets_in_my_bag)):
            ticket_detail = tickets_in_my_bag[i].split("+")
            ids.append(ticket_detail[0])
        tickets = On_Sales.objects.filter(id__in=ids)
        return render_to_response('my_bag.html', locals())
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')


@csrf_exempt
def in_the_bucket(request):  # added new ticket for ticket in my bag
    try:
        adding_time = str(datetime.datetime.now())
        ticket_id = str(request.POST.get('ticket_id'))
        total_number = str(request.POST.get('total_number'))
        ticket = On_Sales.objects.filter(id=ticket_id)[0]
        ticket_name = ticket.title
        img_url = ticket.ticket_photo
        price = ticket.amount_bitcoin
        have_ticket = False
        if request.session.get('tickets_in_my_bag'):
            tickets_in_my_bag = request.session['tickets_in_my_bag']
            for i in range(0, len(tickets_in_my_bag)):
                ticket_detail = tickets_in_my_bag[i].split("+")
                if ticket_detail[0] == ticket_id:
                    have_ticket = True
            if not have_ticket:
                tickets_in_my_bag.append(ticket_id + "+" + total_number
                                         + "+" + adding_time + "+" + unicode(ticket_name)
                                         + "+" + unicode(img_url) + "+" + str(price))
            request.session['tickets_in_my_bag'] = tickets_in_my_bag
        else:
            tickets_in_my_bag = [ticket_id + "+" + total_number
                                 + "+" + adding_time + "+" + unicode(ticket_name)
                                 + "+" + unicode(img_url) + "+" + str(price)]
            request.session['tickets_in_my_bag'] = tickets_in_my_bag
        print tickets_in_my_bag
        return HttpResponse(False, content_type='application/json')
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')

@login_required
def new_order(request, ticket_id):
    try:
        on_sales = On_Sales.objects.filter(id=ticket_id)[0]
        ship_to_user = Member.objects.filter(username=request.user.username)[0]
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')
    total_ticket = 1
    form = new_order_form()
    if request.method == 'POST':
        form = new_order_form(request.POST)
        if form.is_valid():
            try:
                name = request.POST.get('name')
                phone = request.POST.get('phone')
                address = request.POST.get('address')
                order = Orders(on_sales=on_sales, ship_to_user=ship_to_user, total_ticket=total_ticket, status='1',
                               name=name, phone=phone, address=address)
                order.save()
                return HttpResponseRedirect('/bitcoin/payment_page/' + str(order.id))
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry')
    return render_to_response('new_order.html', locals(), context_instance=RequestContext(request))

@login_required
def after_sale_complaint(request, order_id):
    try:
        order = Orders.objects.filter(id=order_id)[0]
    except:
        return HttpResponseRedirect('/sorry')
    form = after_sale_complaint_form(initial={'orders': order})
    if request.method == 'POST':
        form = after_sale_complaint_form(request.POST)
        if form.is_valid():
            try:
                form.save()
                #TODO mailgun: #  __author__ = 'barisariburnu'
                return HttpResponseRedirect('/')
            except:
                return HttpResponseRedirect('/sorry')
    return render_to_response('after_sale_complaint.html', locals(), context_instance=RequestContext(request))