# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Slider'
        db.create_table('slider_slider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('slider', ['Slider'])

        # Adding model 'Slide'
        db.create_table('slider_slide', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slider', self.gf('django.db.models.fields.related.ForeignKey')(related_name='slides', blank=True, to=orm['slider.Slider'])),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('target', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('display', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=100)),
        ))
        db.send_create_signal('slider', ['Slide'])


    def backwards(self, orm):
        
        # Deleting model 'Slider'
        db.delete_table('slider_slider')

        # Deleting model 'Slide'
        db.delete_table('slider_slide')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['slider']
