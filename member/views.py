from django.contrib.auth.decorators import login_required
from django.core.context_processors import request, csrf
from django.views.decorators.csrf import csrf_exempt
from gi.overrides.keysyms import seconds
import time
import datetime
from django.template.loader import get_template

__author__ = 'cemkiy'
__author__ = 'kaykisizcom'
__author__ = 'barisariburnu'

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context
from django.contrib.auth.models import User
from member.forms import *
from django.forms.util import ErrorList
import bag_operations
from member.bag_operations import bag_skeleton
from mailgun import *
import uuid
from django.template.defaultfilters import slugify
# Create your views here.

def new_member(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/member/member_profile/')

    form = new_member_form
    if request.method == 'POST':
        form = new_member_form(request.POST)
        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            member_user_auth = User.objects.create_user(username, email, password)
            member_user_auth.is_staff = False
            member_user_auth.is_active= False
            member_user_auth.save()
            form.save()

            member = User.objects.filter(username=username)[0]
            code = str(uuid.uuid4())
            activation = Activation.objects.create(isuser=True, activivation_code=code, user_or_order_id=member.id)
            activation.save()

            template = get_template("mail_user_activation.html")
            context = Context({'username': username,
                              'email': email,
                              'activation_code': code})
            content = template.render(context)
            mailgun_operator = mailgun()
            mailgun_operator.send_mail_with_html(member_user_auth.email, content)
            return HttpResponseRedirect('/accounts/login/')

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
        if not ticket.active:
            HttpResponseRedirect('/')
        return render_to_response('ticket_details.html', locals(), context_instance=RequestContext(request))
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')


@login_required
def comes_shipping(request):  # user own exchanges
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        orders = Orders.objects.filter(ship_to_user=member, status__in=[2, 3, 4, 5], active=True).all()
        return render_to_response('comes_shipping.html', locals())
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')


@login_required
def sends_shipping(request):  # user 3rd person exchanges
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        orders = Orders.objects.filter(on_sales__member=member, status__in=[2, 3, 4, 5], active=True).all()
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

            cargo_company = request.POST.get('cargo_company')
            cargo_no = request.POST.get('cargo_no')
            user_url_for_btc_send = request.POST.get('user_url_for_btc_send')
            order.cargo_company = cargo_company
            order.cargo_no = cargo_no
            order.user_url_for_btc_send = user_url_for_btc_send
            order.status = '3'
            order.save()

            trace = order.cargo_company
            tracing_link = ""

            if trace == '0':
                tracing_link = 'http://selfservis.yurticikargo.com/reports/SSWDocumentDetail.aspx?DocId=' + str(order.cargo_no)
            elif trace == '1':
                tracing_link = 'http://www.ups.com.tr/WaybillSorgu.aspx?waybill=' + str(order.cargo_no)
            elif trace == '2':
                tracing_link = 'http://kargotakip.araskargo.com.tr/?code=' + str(order.cargo_no)

            template = get_template("mail_send_cargo_no_and_user_url_for_btc_send.html")
            context = Context({'username': order.ship_to_user.username,
                               'ticket_name': order.on_sales.title,
                               'cargo_brand': str(order.get_cargo_company_display) + 'KARGO',
                               'tracing_link': tracing_link,
                               'order_id': order.id})
            content = template.render(context)
            mailgun_operator = mailgun()
            mailgun_operator.send_mail_with_html(order.ship_to_user.email, content)

            return HttpResponseRedirect('/member/sends_shipping/')


    return render_to_response('send_cargo_no_and_user_url_for_btc_send.html', locals(), context_instance=RequestContext(request))

def my_bag(request):  # bag is basket of my take ticket

    #clean bag
    # response = HttpResponse()
    # tickets_in_my_bag = request.COOKIES['tickets_in_my_bag']
    # tickets_in_my_bag = []
    # response.set_cookie('tickets_in_my_bag', tickets_in_my_bag)
    # return response

    tickets = []
    if 'tickets_in_my_bag' in request.COOKIES:
        try:
            tickets_in_my_bag = request.COOKIES['tickets_in_my_bag']
            print tickets_in_my_bag
            ticket = ''
            for letter in tickets_in_my_bag:
                if letter is '?':
                    raw_ticket = bag_skeleton()
                    print ticket
                    raw_ticket.solved_bag_item(ticket)
                    print raw_ticket.total_number
                    tickets.append(raw_ticket)
                    ticket = ''
                else:
                    ticket = ticket + letter
        except Exception as e:
            print e
            return HttpResponseRedirect('/sorry')
        except Exception as e:
            print e
            return HttpResponseRedirect('/sorry')
    return render_to_response('my_bag.html', locals(), context_instance=RequestContext(request))




@csrf_exempt
def in_the_bucket(request):  # added new ticket for ticket in my bag
    response = HttpResponse()
    new_item = bag_skeleton()
    ticket_id = request.POST.get('ticket_id')
    total_number = request.POST.get('total_number')
    ticket = On_Sales.objects.filter(id=ticket_id)[0]

    try:
        new_item.create_bag_item(ticket_id, abs(int(total_number)), ticket.amount_bitcoin, ticket.title.encode('utf-8'), ticket.ticket_photo)
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')

    if 'tickets_in_my_bag' in request.COOKIES:
        tickets_in_my_bag = request.COOKIES['tickets_in_my_bag']
    else:
        tickets_in_my_bag = ''

    tickets_in_my_bag = tickets_in_my_bag + new_item.cokkie_text
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(minutes=30), "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie('tickets_in_my_bag', tickets_in_my_bag, expires=expires)
    return response

@login_required
def new_order(request, ticket_id_and_number):
    #I am a muslim but jesus christ! I love this code part ;) -CK
    ticket_data = '' #total number
    ticket_id = ''
    for letter in ticket_id_and_number:
        if letter == '-':
            ticket_id = ticket_data
            ticket_data = ''
        else:
            ticket_data = ticket_data + letter
    try:
        on_sales = On_Sales.objects.filter(id=ticket_id)[0]
        ship_to_user = Member.objects.filter(username=request.user.username)[0]
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')

    try:
        total_ticket = abs(int(ticket_data))
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')

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
        on_sale = On_Sales.objects.filter(id=order.on_sales.id)[0]
    except:
        return HttpResponseRedirect('/sorry')
    form = after_sale_complaint_form(initial={'orders': order})
    if request.method == 'POST':
        form = after_sale_complaint_form(request.POST)
        if form.is_valid():
            try:
                on_sale.active = False
                on_sale.save()
                order.active = False
                order.save()
                form.save()

                template = get_template("mail_after_sale_complaint.html")
                context = Context({'username': order.ship_to_user.username,
                                   'ticket_name': order.on_sales.title,
                                   'order_id': order.id})
                content = template.render(context)
                mailgun_operator = mailgun()
                mailgun_operator.send_mail_with_html(order.ship_to_user.email, content)

                return HttpResponseRedirect('/')
            except:
                return HttpResponseRedirect('/sorry')
    return render_to_response('after_sale_complaint.html', locals(), context_instance=RequestContext(request))

def user_activation(request, identity):
    try:
        active = Activation.objects.filter(activivation_code=identity)[0]
        user = User.objects.filter(id=active.user_or_order_id)[0]
    except:
        return HttpResponseRedirect('/sorry')
    try:
        if user:
            user.is_active = True
            user.is_staff = True
            user.save()
            active.delete()
            return HttpResponseRedirect('/accounts/login/')
    except:
        return HttpResponseRedirect('/sorry')

@login_required
def vote_activation(request, identity, point):
    try:
        active = Activation.objects.filter(activivation_code=identity)[0]
        member = Member.objects.filter(id=active.user_or_order_id)[0]
    except:
        return HttpResponseRedirect('/sorry')
    try:
        if member:
            if not member.points:
                member.points = 0
            if not member.points_counter:
                member.points_counter = 0
            member.points = ((member.points * member.points_counter) + int(point))/(member.points_counter+1)
            member.points_counter += 1
            member.save()
            active.delete()
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/sorry')