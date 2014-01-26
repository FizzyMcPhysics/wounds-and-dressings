# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Wound.wound_type' to match new field type.
        db.rename_column(u'dressings_wound', 'wound_type', 'wound_type_id')
        # Changing field 'Wound.wound_type'
        db.alter_column(u'dressings_wound', 'wound_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dressings.WoundType']))
        # Adding index on 'Wound', fields ['wound_type']
        db.create_index(u'dressings_wound', ['wound_type_id'])


    def backwards(self, orm):
        # Removing index on 'Wound', fields ['wound_type']
        db.delete_index(u'dressings_wound', ['wound_type_id'])


        # Renaming column for 'Wound.wound_type' to match new field type.
        db.rename_column(u'dressings_wound', 'wound_type_id', 'wound_type')
        # Changing field 'Wound.wound_type'
        db.alter_column(u'dressings_wound', 'wound_type', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dressings.dressing': {
            'Meta': {'ordering': "['name']", 'object_name': 'Dressing'},
            'absorbancy': ('django.db.models.fields.CharField', [], {'default': "'low'", 'max_length': '10'}),
            'adherence': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'anti_microbial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'body_area': ('django.db.models.fields.CharField', [], {'default': "'all'", 'max_length': '10'}),
            'debriding': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'diabetic_safe': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fibrous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'foam': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hydrating': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morphology': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'suitable_for': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dressings.WoundType']", 'symmetrical': 'False'}),
            'topical_agent': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '10'})
        },
        u'dressings.wound': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Wound'},
            'body_area': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'change_frequency': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'diabetic_patient': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'exudate_level': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'heritage': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'patient_nhs_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'wound_age': ('django.db.models.fields.CharField', [], {'default': "'fresh'", 'max_length': '50'}),
            'wound_classification': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'wound_depth': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'wound_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dressings.WoundType']"})
        },
        u'dressings.woundtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'WoundType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['dressings']