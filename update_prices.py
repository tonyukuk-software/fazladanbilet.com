#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Unicode - Django
__author__ = 'cemkiy'
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jackalprojects.settings")
from member.models import On_Sales
from bitcoin.models import Bitcoin_Price
from btcturk_client.client import Btcturk

def main():
    btcturk = Btcturk()
    now_price = float(btcturk.ticker()['ask'])
    print now_price
    btc_price = Bitcoin_Price.objects.all()
    tickets = On_Sales.objects.filter(active=True)
    if btc_price:
        past_price = btc_price[0].past_price
        btc_price[0].past_price = now_price
        btc_price[0].save()
        print past_price

        for control_ticket in tickets:
            new_amount = (now_price * control_ticket.amount_bitcoin) / (past_price)
            control_ticket.amount_bitcoin = new_amount
            control_ticket.save()
    else:
        past_price = now_price
        new_btc_price = Bitcoin_Price.objects.create(past_price=now_price)
        new_btc_price.save()
        print 'new'
        print past_price



if __name__ == "__main__":
    main()
