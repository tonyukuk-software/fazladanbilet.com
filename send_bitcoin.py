__author__ = 'cemkiy'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Unicode - Django

from decimal import Decimal
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jackalprojects.settings")
from member.models import Orders
from bitcoin import coinbase_api


def main():
    coinbase_operator = coinbase_api()
    orders = Orders.objects.filter(status='4', active=True).all()
    for order in orders:
        amount = Decimal(order.on_sales.amount_bitcoin) * int(order.total_ticket)
        print amount
        try:
            coinbase_operator.send_bitcoin(order.user_url_for_btc_send, amount)
        except Exception as e:
            print e


if __name__ == "__main__":
    main()