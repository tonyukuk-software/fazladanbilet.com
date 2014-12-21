from django.template.loader import get_template
from mailgun import mailgun

__author__ = 'cemkiy'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Unicode - Django

from decimal import Decimal, Context
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jackalprojects.settings")
from member.models import Orders
from bitcoin import coinbase_api


def main():
    coinbase_operator = coinbase_api()
    orders = Orders.objects.filter(status='4', active=True).all()
    for order in orders:
        amount = Decimal(order.on_sales.amount_bitcoin) * int(order.total_ticket)
        comission = Decimal(amount/20)
        amount = amount - comission # without comission
        print amount
        try:
            coinbase_operator.send_bitcoin(order.user_url_for_btc_send, amount)
        except Exception as e:
            print e
        template = get_template("mail_send_bitcoin.html")
        context = Context({'username': order.on_sales.member.username,
                           'ticket_name': order.on_sales.title,
                           'bitcoin_url': order.user_url_for_btc_send,
                           'amount': amount}) #send amount
        content = template.render(context)
        mailgun_operator = mailgun()
        mailgun_operator.send_mail_with_html(order.on_sales.member.email, content)


if __name__ == "__main__":
    main()