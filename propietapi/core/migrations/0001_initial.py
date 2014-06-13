# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('core_user_profile', (
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='profile', unique=True, primary_key=True, to=orm['auth.User'])),
            ('phone', self.gf('django.db.models.fields.TextField')(max_length=40)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True)),
            ('activation_key', self.gf('django.db.models.fields.CharField')(default=None, max_length=40, null=True, blank=True)),
            ('key_expires', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['UserProfile'])

        # Adding model 'Feature'
        db.create_table('core_feature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Feature'])

        # Adding model 'Operation'
        db.create_table('core_operation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_index=True)),
            ('operation', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Operation'])

        # Adding model 'Currency'
        db.create_table('core_currency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_index=True)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Currency'])

        # Adding model 'Service'
        db.create_table('core_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Service'])

        # Adding model 'Category'
        db.create_table('core_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Category'])

        # Adding model 'SubCategory'
        db.create_table('core_sub_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_index=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['SubCategory'])

        # Adding model 'Ambience'
        db.create_table('core_ambience', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Ambience'])

        # Adding model 'Location'
        db.create_table('core_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_index=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('longitude', self.gf('django.db.models.fields.CharField')(default=0, max_length=100, null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(default=0, max_length=100, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Country'], null=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Region'], null=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.City'], null=True)),
        ))
        db.send_create_signal('core', ['Location'])

        # Adding model 'Property'
        db.create_table('core_property', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Category'])),
            ('subcategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.SubCategory'], null=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('antiqueness', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, blank=True)),
            ('square_meters', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('total_covered_meters', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('total_uncovered_meters', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Location'], unique=True)),
            ('lightness', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, blank=True)),
            ('orientation', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, blank=True)),
            ('disposition', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, blank=True)),
            ('quantityAmbiences', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, blank=True)),
            ('quantityBathrooms', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, blank=True)),
            ('quantityBedrooms', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, blank=True)),
            ('quantityGarages', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, blank=True)),
            ('garageCoverage', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True, blank=True)),
            ('buildingType', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, blank=True)),
            ('buildingStatus', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, blank=True)),
            ('buildingCategory', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, blank=True)),
            ('apartmentsPerFloor', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('quantityBuildingFloors', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('floorNumber', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('quantityElevators', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, blank=True)),
            ('expenses', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('roofType', self.gf('django.db.models.fields.CharField')(default=0, max_length=1, blank=True)),
            ('industrialRoofType', self.gf('django.db.models.fields.CharField')(default=0, max_length=1, blank=True)),
            ('roofHeight', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('gateType', self.gf('django.db.models.fields.CharField')(default=0, max_length=1, blank=True)),
            ('frontGround', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('largeGround', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('hectares', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('fot', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('fos', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('stage', self.gf('django.db.models.fields.CharField')(default=0, max_length=1, blank=True)),
            ('deliveryYear', self.gf('django.db.models.fields.CharField')(default=0, max_length=1, blank=True)),
            ('suitableProfessional', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, blank=True)),
            ('commercialUsage', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, blank=True)),
            ('suitableCredit', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, null=True, blank=True)),
            ('providesFunding', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Property'])

        # Adding M2M table for field features on 'Property'
        m2m_table_name = db.shorten_name('core_property_features')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('property', models.ForeignKey(orm['core.property'], null=False)),
            ('feature', models.ForeignKey(orm['core.feature'], null=False))
        ))
        db.create_unique(m2m_table_name, ['property_id', 'feature_id'])

        # Adding M2M table for field services on 'Property'
        m2m_table_name = db.shorten_name('core_property_services')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('property', models.ForeignKey(orm['core.property'], null=False)),
            ('service', models.ForeignKey(orm['core.service'], null=False))
        ))
        db.create_unique(m2m_table_name, ['property_id', 'service_id'])

        # Adding M2M table for field ambiences on 'Property'
        m2m_table_name = db.shorten_name('core_property_ambiences')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('property', models.ForeignKey(orm['core.property'], null=False)),
            ('ambience', models.ForeignKey(orm['core.ambience'], null=False))
        ))
        db.create_unique(m2m_table_name, ['property_id', 'ambience_id'])

        # Adding model 'Post'
        db.create_table('core_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_index=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Property'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='post_user', to=orm['auth.User'])),
            ('agent', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='post_agent', null=True, blank=True, to=orm['auth.User'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Category'])),
            ('operation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Operation'])),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Currency'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('hidden_note', self.gf('django.db.models.fields.TextField')(default=None, max_length=500, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('video_url', self.gf('django.db.models.fields.URLField')(default=None, max_length=500, null=True, blank=True)),
            ('map_image_url', self.gf('django.db.models.fields.URLField')(default=None, max_length=500, null=True, blank=True)),
            ('plane_url', self.gf('django.db.models.fields.URLField')(default=None, max_length=500, null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.Region'], null=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.City'], null=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('core', ['Post'])

        # Adding model 'PostPhoto'
        db.create_table('core_post_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_index=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.Post'], blank=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('file', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100)),
        ))
        db.send_create_signal('core', ['PostPhoto'])

        # Adding model 'SavedQuery'
        db.create_table('core_saved_query', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('query', self.gf('django.db.models.fields.TextField')()),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('core', ['SavedQuery'])

        # Adding model 'Alert'
        db.create_table('core_alert', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('query', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.SavedQuery'], unique=True)),
            ('alert_type', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('core', ['Alert'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('core_user_profile')

        # Deleting model 'Feature'
        db.delete_table('core_feature')

        # Deleting model 'Operation'
        db.delete_table('core_operation')

        # Deleting model 'Currency'
        db.delete_table('core_currency')

        # Deleting model 'Service'
        db.delete_table('core_service')

        # Deleting model 'Category'
        db.delete_table('core_category')

        # Deleting model 'SubCategory'
        db.delete_table('core_sub_category')

        # Deleting model 'Ambience'
        db.delete_table('core_ambience')

        # Deleting model 'Location'
        db.delete_table('core_location')

        # Deleting model 'Property'
        db.delete_table('core_property')

        # Removing M2M table for field features on 'Property'
        db.delete_table(db.shorten_name('core_property_features'))

        # Removing M2M table for field services on 'Property'
        db.delete_table(db.shorten_name('core_property_services'))

        # Removing M2M table for field ambiences on 'Property'
        db.delete_table(db.shorten_name('core_property_ambiences'))

        # Deleting model 'Post'
        db.delete_table('core_post')

        # Deleting model 'PostPhoto'
        db.delete_table('core_post_photo')

        # Deleting model 'SavedQuery'
        db.delete_table('core_saved_query')

        # Deleting model 'Alert'
        db.delete_table('core_alert')


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
        u'cities_light.city': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('region', 'name'), ('region', 'slug'))", 'object_name': 'City'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'feature_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'population': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True', 'blank': 'True'}),
            'search_names': ('cities_light.models.ToSearchTextField', [], {'default': "''", 'max_length': '4000', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        u'cities_light.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'code2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'code3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'tld': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        },
        u'cities_light.region': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('country', 'name'), ('country', 'slug'))", 'object_name': 'Region'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.alert': {
            'Meta': {'object_name': 'Alert'},
            'alert_type': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'query': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.SavedQuery']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'core.ambience': {
            'Meta': {'object_name': 'Ambience'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.currency': {
            'Meta': {'object_name': 'Currency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'core.feature': {
            'Meta': {'object_name': 'Feature'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.City']", 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Country']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True'})
        },
        'core.operation': {
            'Meta': {'object_name': 'Operation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'operation': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.post': {
            'Meta': {'object_name': 'Post'},
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'post_agent'", 'null': 'True', 'blank': 'True', 'to': u"orm['auth.User']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Category']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.City']", 'null': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Currency']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hidden_note': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'map_image_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Operation']"}),
            'plane_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Property']"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_light.Region']", 'null': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'post_user'", 'to': u"orm['auth.User']"}),
            'video_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        'core.postphoto': {
            'Meta': {'object_name': 'PostPhoto', 'db_table': "'core_post_photo'"},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['core.Post']", 'blank': 'True'})
        },
        'core.property': {
            'Meta': {'object_name': 'Property'},
            'ambiences': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Ambience']", 'symmetrical': 'False', 'blank': 'True'}),
            'antiqueness': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'apartmentsPerFloor': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'buildingCategory': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'buildingStatus': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'buildingType': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Category']"}),
            'commercialUsage': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deliveryYear': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'disposition': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'expenses': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Feature']", 'symmetrical': 'False', 'blank': 'True'}),
            'floorNumber': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'fos': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'fot': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'frontGround': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'garageCoverage': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'gateType': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'hectares': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'industrialRoofType': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'largeGround': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lightness': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Location']", 'unique': 'True'}),
            'orientation': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'providesFunding': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'quantityAmbiences': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'quantityBathrooms': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'quantityBedrooms': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'quantityBuildingFloors': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'quantityElevators': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'quantityGarages': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'roofHeight': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'roofType': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Service']", 'symmetrical': 'False', 'blank': 'True'}),
            'square_meters': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'stage': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.SubCategory']", 'null': 'True'}),
            'suitableCredit': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'suitableProfessional': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1', 'blank': 'True'}),
            'total_covered_meters': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'total_uncovered_meters': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'core.savedquery': {
            'Meta': {'object_name': 'SavedQuery', 'db_table': "'core_saved_query'"},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'query': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'core.service': {
            'Meta': {'object_name': 'Service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.subcategory': {
            'Meta': {'object_name': 'SubCategory', 'db_table': "'core_sub_category'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.userprofile': {
            'Meta': {'object_name': 'UserProfile', 'db_table': "'core_user_profile'"},
            'activation_key': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'key_expires': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.TextField', [], {'max_length': '40'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['core']