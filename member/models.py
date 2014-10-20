from django.db import models

# Create your models here.

class Publisher(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=20)
    total_money = models.PositiveIntegerField(default=0, editable=False)
    active = models.BooleanField(default=True, editable=False)
    cdate = models.DateTimeField(auto_now_add=True)

class Member(models.Model):
    username = models.CharField(max_length=50, unique=True, editable=False)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True, editable=False)
    city = models.CharField(max_length=20)
    active = models.BooleanField(default=True, editable=False)
    cdate = models.DateTimeField(auto_now_add=True)

class Wallet(models.Model):
    member = models.ForeignKey(Member)

class On_Sales(models.Model):
    member = models.ForeignKey(Member)
    total_ticket = models.PositiveIntegerField(default=0)
    amount_bitcoin = models.FloatField(default=0)
    cdate = models.DateTimeField(auto_now_add=True)
    edate = models.DateTimeField()
    active = models.BooleanField(default=True, editable=False)

class Orders(models.Model):
    on_sales = models.ForeignKey(On_Sales)
    ship_to_user = models.ForeignKey(Member)
    status = models.PositiveIntegerField(default=0) #options
    adress = models.CharField(max_length=256)
    cargo_company = models.PositiveIntegerField(default=0) #options
    cargo_no = models.CharField(max_length=256)
    active = models.BooleanField(default=True, editable=False)
    cdate = models.DateTimeField(auto_now_add=True)



