__author__ = 'cemkiy'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Unicode - Django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jackalprojects.settings")
from member.models import Orders
from cargo_api import *

def main():
    cargo_controller = cargo_api()
    orders = Orders.objects.filter(status='3').all()
    for order in orders:
        if order.cargo_company == '0':
            if cargo_controller.yurtici(order.cargo_no):
                order.status = '4'
                order.save()
        elif order.cargo_company == '1':
            if cargo_controller.ups(order.cargo_no):
                order.status = '4'
                order.save()
        else:
            if cargo_controller.aras(order.cargo_no):
                order.status = '4'
                order.save()


if __name__ == "__main__":
    main()