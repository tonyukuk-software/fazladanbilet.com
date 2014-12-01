from django.shortcuts import render, render_to_response
# Create your views here.
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
    #button = api.create_button(amount, order_id)
    print api.get_orders()
    #button_data = button[0]
    return render_to_response('payment_page.html', locals())


def succes_url(request, order_id):
    pass

def cancel_url(request):
    return render_to_response('cancel_url.html', locals())