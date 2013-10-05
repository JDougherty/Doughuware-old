# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Tag.parent'
        db.alter_column(u'core_tag', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Tag'], null=True))

    def backwards(self, orm):

        # Changing field 'Tag.parent'
        db.alter_column(u'core_tag', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['core.Tag']))

    models = {
        u'core.document': {
            'Meta': {'object_name': 'Document'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'preview': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'core.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Tag']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']