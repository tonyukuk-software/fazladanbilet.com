from cups import require
from jackalprojects import settings

__author__ = 'cemkiy'

from django.db import models

# Create your models here.

class Member(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    profile_photo = models.ImageField(null=True, upload_to="profile_photos/")
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
    image_url = models.URLField()
    amount_bitcoin = models.FloatField(default=0)
    cdate = models.DateTimeField(auto_now_add=True)
    edate = models.DateTimeField()
    active = models.BooleanField(default=True, editable=False)

class Orders(models.Model):
    on_sales = models.ForeignKey(On_Sales)
    ship_to_user = models.OneToOneField(Member)
    status = models.PositiveIntegerField(default=0) #options
    adress = models.CharField(max_length=256)
    cargo_company = models.PositiveIntegerField(default=0) #options
    cargo_no = models.CharField(max_length=256)
    active = models.BooleanField(default=True, editable=False)
    cdate = models.DateTimeField(auto_now_add=True)

class After_Sale(models.Model): #Feedback from shiping members
    orders = models.OneToOneField(Orders)
    status = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=500)
    cdate = models.DateField(auto_now_add=True)




