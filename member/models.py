from jackalprojects import settings

__author__ = 'cemkiy'
__author__ = 'barisariburnu'
__author__ = 'kaykisizcom'

from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.

class Member(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    profile_photo = models.ImageField(null=True, blank=True, upload_to="profile_photos/")
    points = models.FloatField(default=0.0, blank=True, null=True)
    points_counter = models.PositiveIntegerField(default=0, blank=True, null=True) #how many peoples give vote
    active = models.BooleanField(default=True, editable=False)
    cdate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.username

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
    total_ticket = models.SmallIntegerField(default=0)
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
    (u'0', _(u'cancel')),
    (u'1', _(u'waiting_for_payment')),
    (u'2', _(u'waiting_for_cargo')),
    (u'3', _(u'on_the_road')),
    (u'4', _(u'success_shipping')),
    (u'5', _(u'failure_shipping'))
    )

    CARGO_CHOICES = (
    (u'0', u'yurtici'),
    (u'1', u'ups'),
    (u'2', u'aras'),
    (u'3', u''),
    )

    on_sales = models.ForeignKey(On_Sales)
    ship_to_user = models.ForeignKey(Member)
    total_ticket = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1') #options
    name = models.CharField(max_length=50, default='', null=True)
    phone = models.CharField(max_length=11, default='', null=True)
    address = models.CharField(max_length=256, default='', null=True)
    cargo_company = models.CharField(max_length=1, choices=CARGO_CHOICES, default='3', null=True) #options
    cargo_no = models.CharField(max_length=256, default=0, null=True)
    user_url_for_btc_send = models.CharField(max_length=27, default='', null=True)
    active = models.BooleanField(default=True, editable=False)
    cdate = models.DateTimeField(auto_now_add=True)

class After_Sale(models.Model): #Feedback from shiping members

    REPORT_CHOICES = (
    (u'0', _(u'cargo_problem')),
    (u'1', _(u'wrong_ticket')),
    (u'2', _(u'fake_ticket')),
    (u'3', _(u'bitcoin_problem')),
    (u'4', _(u'other')),
    )

    orders = models.OneToOneField(Orders)
    status = models.CharField(max_length=1, choices=REPORT_CHOICES, default='0') #options
    description = models.CharField(max_length=500)
    cdate = models.DateField(auto_now_add=True)

class Activation(models.Model):
    isuser = models.BooleanField(default=True)
    activivation_code = models.CharField(max_length=36, null=True)
    user_or_order_id = models.CharField(max_length=6, default='1', null=True)


