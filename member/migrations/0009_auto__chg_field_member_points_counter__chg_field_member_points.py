# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Member.points_counter'
        db.alter_column(u'member_member', 'points_counter', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Member.points'
        db.alter_column(u'member_member', 'points', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Member.points_counter'
        db.alter_column(u'member_member', 'points_counter', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'Member.points'
        db.alter_column(u'member_member', 'points', self.gf('django.db.models.fields.PositiveIntegerField')())

    models = {
        u'member.after_sale': {
            'Meta': {'object_name': 'After_Sale'},
            'cdate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orders': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['member.Orders']", 'unique': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'})
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
            'points': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'points_counter': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'profile_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'member.on_sales': {
            'Meta': {'object_name': 'On_Sales'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amount_bitcoin': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Category']"}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'edate': ('django.db.models.fields.DateTimeField', [], {}),
            'from_city': ('django.db.models.fields.related.ForeignKey', [], {'default': "'0'", 'to': u"orm['member.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Member']"}),
            'ticket_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total_ticket': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'member.orders': {
            'Meta': {'object_name': 'Orders'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'adress': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256'}),
            'cargo_company': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'cargo_no': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'on_sales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.On_Sales']"}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '11'}),
            'ship_to_user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['member.Member']", 'unique': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '1'}),
            'total_ticket': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        u'member.wallet': {
            'Meta': {'object_name': 'Wallet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['member.Member']", 'unique': 'True'})
        }
    }

    complete_apps = ['member']