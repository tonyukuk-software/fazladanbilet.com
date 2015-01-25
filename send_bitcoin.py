#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Unicode - Django
__author__ = 'cemkiy'
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jackalprojects.settings")
from member.models import Orders
from django.template.loader import get_template
import decimal
from bitcoin.coinbase_api import coinbase_api
from mailgun import mailgun
from django.template import Context
from coinbase import CoinbaseAmount
from decimal import Decimal

def main():
    coinbase_operator = coinbase_api()
    orders = Orders.objects.filter(status='4', active=True).all()
    for order in orders:
        amount = Decimal(order.on_sales.amount_bitcoin) * int(order.total_ticket)
        print amount
        comission = amount/10
        comission = comission + Decimal(0.0001)
        print comission
        amount = amount - comission # without comission
        print amount
        try:
            c_amount = CoinbaseAmount(amount, 'BTC')
            coinbase_operator.send_bitcoin(adress=order.user_url_for_btc_send, amount=c_amount, note='fazladanbilet sends your bitcoin')
            template = get_template("mail_send_bitcoin.html")
            context = Context({'username': order.on_sales.member.username,
                               'ticket_name': order.on_sales.title,
                               'bitcoin_url': order.user_url_for_btc_send,
                               'amount': amount}) #send amount
            content = template.render(context)
            mailgun_operator = mailgun()
            mailgun_operator.send_mail_with_html(order.on_sales.member.email, content)
        except Exception as e:
            print e
            mailgun_operator = mailgun()
            text = str(order.id)+' '+str(order.on_sales.member.username)+' failure payment'
            mailgun_operator.send_mail('info@fazladanbilet.com', text)


if __name__ == "__main__":
    main()