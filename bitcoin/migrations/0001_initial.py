# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bitcoin_Price'
        db.create_table(u'bitcoin_bitcoin_price', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('past_price', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal(u'bitcoin', ['Bitcoin_Price'])


    def backwards(self, orm):
        # Deleting model 'Bitcoin_Price'
        db.delete_table(u'bitcoin_bitcoin_price')


    models = {
        u'bitcoin.bitcoin_price': {
            'Meta': {'object_name': 'Bitcoin_Price'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'past_price': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        }
    }

    complete_apps = ['bitcoin']