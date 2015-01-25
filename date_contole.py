#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Unicode - Django
__author__ = 'cemkiy'
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jackalprojects.settings")
from member.models import On_Sales
from datetime import date

def main():
    tickets = On_Sales.objects.filter(active=True)
    for control_ticket in tickets:
        if control_ticket.edate.day == date.today().day and control_ticket.edate.month == date.today().month and control_ticket.edate.year == date.today().year:
            control_ticket.active = False
            control_ticket.save()

if __name__ == "__main__":
    main()
