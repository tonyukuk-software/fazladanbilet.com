from django.template.loader import get_template
from mailgun import mailgun

__author__ = 'cemkiy'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Unicode - Django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jackalprojects.settings")
from member.models import Orders, Activation
from cargo_api import *
from django.template import Context
import uuid

def main():
    cargo_controller = cargo_api()
    orders = Orders.objects.filter(status='3', active=True).all()
    for order in orders:
        if order.cargo_company == '0':
            if cargo_controller.yurtici(order.cargo_no):
                try:
                    order.status = '4'
                    order.save()
                    send_mail(order)
                except Exception as e:
                    print e
        elif order.cargo_company == '1':
            if cargo_controller.ups(order.cargo_no):
                try:
                    order.status = '4'
                    order.save()
                    send_mail(order)
                except Exception as e:
                    print e
        else:
            if cargo_controller.aras(order.cargo_no):
                try:
                    order.status = '4'
                    order.save()
                    send_mail(order)
                except Exception as e:
                    print e

def send_mail(order):
    code = str(uuid.uuid4())
    activation = Activation.objects.create(isuser=False, activivation_code=code, user_or_order_id=order.id)
    activation.save()

    template = get_template("mail_vote.html")
    context = Context({'username': order.ship_to_user.username,
                       'ticket_name': order.on_sales.title,
                       'order_id': order.id})
    content = template.render(context)
    mailgun_operator = mailgun()
    mailgun_operator.send_mail_with_html('barisariburnu@gmail.com', content)

if __name__ == "__main__":
    main()