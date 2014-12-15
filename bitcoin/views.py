__author__ = 'cemkiy'

from django.shortcuts import render, render_to_response
# Create your views here.
from django.http.response import HttpResponse, HttpResponseRedirect
from bitcoin.coinbase_api import coinbase_api
from member.models import Orders, On_Sales
from decimal import *

def exeample(request):

    api = coinbase_api()
    button = api.create_button('1', 'deneme', '31')
    print button[0]

    return render_to_response('main.html', locals())

def payment_page(request, order_id):
    try:
        order = Orders.objects.filter(id=order_id)[0]
    except Exception as e:
        print e
        return False

    amount = Decimal(order.on_sales.amount_bitcoin) * int(order.total_ticket)
    print amount
    api = coinbase_api()
    button = api.create_button(amount, order_id)
    print api.get_orders()
    button_data = button[0]
    return render_to_response('payment_page.html', locals())


def succes_url(request, order_id):
    try:
        order = Orders.objects.filter(id=order_id)[0]
        on_sale = On_Sales.objects.filter(id=order.on_sales.id)[0]
    except Exception as e:
        print e
        return False

    api = coinbase_api()
    coinbase_order = api.get_order_by_id(order_id)

    if coinbase_order:
        print coinbase_order[2]
        if str(coinbase_order[2]) == 'Status.completed':
            try:
                order.status = '2' #next step for dealing
                order.save()
            except Exception as e:
                print e
                return False

            try:
                on_sale.total_ticket = on_sale.total_ticket - order.total_ticket #decrease total ticket
                if on_sale.total_ticket == 0:
                    on_sale.active = False
                on_sale.save()
            except Exception as e:
                print e
                return False

            #TODO mailgun:send mails to ticket owner and ship_to_user __author__ = 'barisariburnu'

        else:
            return HttpResponseRedirect('/bitcoin/cancel_url')

    return render_to_response('success_url.html', locals())


def cancel_url(request):
    return render_to_response('cancel_url.html', locals())