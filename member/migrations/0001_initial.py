# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table(u'member_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('points', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('points_counter', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'member', ['Member'])

        # Adding model 'Wallet'
        db.create_table(u'member_wallet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Member'])),
        ))
        db.send_create_signal(u'member', ['Wallet'])

        # Adding model 'Category'
        db.create_table(u'member_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'member', ['Category'])

        # Adding model 'On_Sales'
        db.create_table(u'member_on_sales', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Member'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Category'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('total_ticket', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('based_city', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('amount_bitcoin', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('edate', self.gf('django.db.models.fields.DateTimeField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'member', ['On_Sales'])

        # Adding model 'Orders'
        db.create_table(u'member_orders', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('on_sales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.On_Sales'])),
            ('ship_to_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Member'])),
            ('status', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('adress', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('cargo_company', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('cargo_no', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'member', ['Orders'])

        # Adding model 'After_Sale'
        db.create_table(u'member_after_sale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orders', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Orders'])),
            ('status', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('cdate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'member', ['After_Sale'])

        # Adding model 'City'
        db.create_table(u'member_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city_name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'member', ['City'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table(u'member_member')

        # Deleting model 'Wallet'
        db.delete_table(u'member_wallet')

        # Deleting model 'Category'
        db.delete_table(u'member_category')

        # Deleting model 'On_Sales'
        db.delete_table(u'member_on_sales')

        # Deleting model 'Orders'
        db.delete_table(u'member_orders')

        # Deleting model 'After_Sale'
        db.delete_table(u'member_after_sale')

        # Deleting model 'City'
        db.delete_table(u'member_city')


    models = {
        u'member.after_sale': {
            'Meta': {'object_name': 'After_Sale'},
            'cdate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orders': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Orders']"}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'member.category': {
            'Meta': {'object_name': 'Category'},
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'member.city': {
            'Meta': {'object_name': 'City'},
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'member.member': {
            'Meta': {'object_name': 'Member'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'points_counter': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'member.on_sales': {
            'Meta': {'object_name': 'On_Sales'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amount_bitcoin': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'based_city': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Category']"}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'edate': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Member']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total_ticket': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'member.orders': {
            'Meta': {'object_name': 'Orders'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'cargo_company': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cargo_no': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'on_sales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.On_Sales']"}),
            'ship_to_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Member']"}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'member.wallet': {
            'Meta': {'object_name': 'Wallet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Member']"})
        }
    }

    complete_apps = ['member']