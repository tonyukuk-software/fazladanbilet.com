#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Unicode - Django
__author__ = 'mehmet'
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jackalprojects.settings")
from member.models import Orders

def main():#run at 09:00 pm
    Orders.objects.filter(status='4', active=True).all().delete()

if __name__ == "__main__":
    main()