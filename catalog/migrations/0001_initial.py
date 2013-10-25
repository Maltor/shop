# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'catalog_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['catalog.Category'])),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('meta_desc', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('meta_key', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=200, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'catalog', ['Category'])

        # Adding model 'Product'
        db.create_table(u'catalog_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('meta_desc', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('meta_key', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=200, blank=True)),
            ('short_text', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('full_text', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'catalog', ['Product'])

        # Adding M2M table for field parent on 'Product'
        m2m_table_name = db.shorten_name(u'catalog_product_parent')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'catalog.product'], null=False)),
            ('category', models.ForeignKey(orm[u'catalog.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'category_id'])

        # Adding model 'ProductImages'
        db.create_table(u'catalog_productimages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Product'], null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=200, blank=True)),
        ))
        db.send_create_signal(u'catalog', ['ProductImages'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'catalog_category')

        # Deleting model 'Product'
        db.delete_table(u'catalog_product')

        # Removing M2M table for field parent on 'Product'
        db.delete_table(db.shorten_name(u'catalog_product_parent'))

        # Deleting model 'ProductImages'
        db.delete_table(u'catalog_productimages')


    models = {
        u'catalog.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'meta_desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'meta_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['catalog.Category']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'catalog.product': {
            'Meta': {'object_name': 'Product'},
            'full_text': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'meta_desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'meta_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'cat'", 'symmetrical': 'False', 'to': u"orm['catalog.Category']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'short_text': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        u'catalog.productimages': {
            'Meta': {'object_name': 'ProductImages'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Product']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['catalog']