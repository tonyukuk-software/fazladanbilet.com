from cups import require
from jackalprojects import settings

__author__ = 'cemkiy'

from django.db import models

# Create your models here.

class Member(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    profile_photo = models.ImageField(null=True, blank=True, upload_to="profile_photos/")
    points = models.PositiveIntegerField(default=0)
    points_counter = models.PositiveIntegerField(default=0) #how many peoples give vote
    active = models.BooleanField(default=True, editable=False)
    cdate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.username

class Wallet(models.Model):
    member = models.OneToOneField(Member)

class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.category_name

class City(models.Model):
    city_name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.city_name

class On_Sales(models.Model):
    member = models.ForeignKey(Member)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    total_ticket = models.PositiveIntegerField(default=0)
    from_city = models.ForeignKey(City, default='0')
    ticket_photo = models.ImageField(null=True, upload_to="ticket_photos/")
    amount_bitcoin = models.FloatField(default=0)
    cdate = models.DateTimeField(auto_now_add=True)
    edate = models.DateTimeField()
    active = models.BooleanField(default=True, editable=False)

    def __unicode__(self):
        return self.member.username + self.title

class Orders(models.Model):

    STATUS_CHOICES = (
    (u'0', u'cancel'),
    (u'1', u'awaiting'),
    (u'2', u'waiting_for_cargo'),
    (u'3', u'on_the_road'),
    (u'4', u'success_shipping'),
    (u'5', u'failure_shipping')
    )

    CARGO_CHOICES = (
    (u'0', u'yurtici'),
    (u'1', u'mng'),
    (u'2', u'ups'),
    (u'3', u'aras'),
    (u'4', u'ptt'),
    )

    on_sales = models.ForeignKey(On_Sales)
    ship_to_user = models.OneToOneField(Member)
    total_ticket = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1') #options
    name = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=11, default='')
    adress = models.CharField(max_length=256, default='')
    cargo_company = models.CharField(max_length=1, choices=CARGO_CHOICES, default='0') #options
    cargo_no = models.CharField(max_length=256)
    active = models.BooleanField(default=True, editable=False)
    cdate = models.DateTimeField(auto_now_add=True)

class After_Sale(models.Model): #Feedback from shiping members

    REPORT_CHOICES = (
    (u'0', u'cargo_problem'),
    (u'1', u'wrong_ticket'),
    (u'2', u'fake_ticket'),
    (u'3', u'bitcoin_problem'),
    (u'4', u'other'),
    )

    orders = models.OneToOneField(Orders)
    status = models.CharField(max_length=1, choices=REPORT_CHOICES, default='0') #options
    description = models.CharField(max_length=500)
    cdate = models.DateField(auto_now_add=True)




