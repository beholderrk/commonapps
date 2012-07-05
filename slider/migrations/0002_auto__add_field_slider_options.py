# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Slider.options'
        db.add_column('slider_slider', 'options', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Slider.options'
        db.delete_column('slider_slider', 'options')


    models = {
        'slider.slide': {
            'Meta': {'ordering': "('-position',)", 'object_name': 'Slide'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'slider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'blank': 'True', 'to': "orm['slider.Slider']"}),
            'target': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'})
        },
        'slider.slider': {
            'Meta': {'object_name': 'Slider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'options': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['slider']
