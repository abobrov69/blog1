# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Publication'
        db.create_table(u'blog1_publication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'blog1', ['Publication'])


    def backwards(self, orm):
        # Deleting model 'Publication'
        db.delete_table(u'blog1_publication')


    models = {
        u'blog1.publication': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Publication'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['blog1']