# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Location.number'
        db.delete_column('core_location', 'number')


    def backwards(self, orm):
        # Adding field 'Location.number'
        db.add_column('core_location', 'number',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=10),
                      keep_default=False)


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cities_light.city': {
            'Meta': {'unique_together': "(('region', 'name'),)", 'object_name': 'City'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Region']", 'null': 'True', 'blank': 'True'}),
            'search_names': ('cities_light.models.ToSearchTextField', [], {'default': "''", 'max_length': '4000', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        'cities_light.country': {
            'Meta': {'object_name': 'Country'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'code2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'code3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'tld': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        },
        'cities_light.region': {
            'Meta': {'unique_together': "(('country', 'name'),)", 'object_name': 'Region'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.alert': {
            'Meta': {'object_name': 'Alert'},
            'alert_type': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'query': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.SavedQuery']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
        'core.consultingroom': {
            'Meta': {'object_name': 'ConsultingRoom', 'db_table': "'core_property_consulting_room'", '_ormbases': ['core.Property']},
            'apartmentsPerFloor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'buildingCategory': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingCondition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingStatus': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'disposition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'expenses': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'floorNumber': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'garageCoverage': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lightness': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'orientation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Property']", 'unique': 'True', 'primary_key': 'True'}),
            'quantityBathrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBuildingFloors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantityElevators': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityGarages': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'})
        },
        'core.countryhouse': {
            'Meta': {'object_name': 'CountryHouse', 'db_table': "'core_property_country_house'", '_ormbases': ['core.Property']},
            'buildingStatus': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'frontGround': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'largeGround': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lightness': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'orientation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Property']", 'unique': 'True', 'primary_key': 'True'}),
            'quantityBathrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBedrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityFloors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'roofType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'})
        },
        'core.currency': {
            'Meta': {'object_name': 'Currency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'core.department': {
            'Meta': {'object_name': 'Department', 'db_table': "'core_property_department'", '_ormbases': ['core.Property']},
            'apartmentsPerFloor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'buildingCategory': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingCondition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingStatus': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'commercialUsage': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'disposition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'expenses': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'floorNumber': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'garageCoverage': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lightness': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'orientation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Property']", 'unique': 'True', 'primary_key': 'True'}),
            'quantityAmbiences': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBathrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBedrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBuildingFloors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantityElevators': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityGarages': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'suitableProfessional': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'unityType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'})
        },
        'core.feature': {
            'Meta': {'object_name': 'Feature'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.field': {
            'Meta': {'object_name': 'Field', 'db_table': "'core_property_field'", '_ormbases': ['core.Property']},
            'hectares': ('django.db.models.fields.FloatField', [], {}),
            'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Property']", 'unique': 'True', 'primary_key': 'True'})
        },
        'core.garage': {
            'Meta': {'object_name': 'Garage', 'db_table': "'core_property_garage'", '_ormbases': ['core.Property']},
            'expenses': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'garageCoverage': ('django.db.models.fields.FloatField', [], {}),
            'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Property']", 'unique': 'True', 'primary_key': 'True'})
        },
        'core.house': {
            'Meta': {'object_name': 'House', 'db_table': "'core_property_house'", '_ormbases': ['core.Property']},
            'buildingStatus': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'commercialUsage': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'lightness': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'orientation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Property']", 'unique': 'True', 'primary_key': 'True'}),
            'quantityBathrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBedrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityFloors': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'roofType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'})
        },
        'core.industrialbuilding': {
            'Meta': {'object_name': 'IndustrialBuilding', 'db_table': "'core_property_industrial_building'", '_ormbases': ['core.Property']},
            'apartmentsPerFloor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'buildingCategory': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingCondition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingStatus': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'commercialUsage': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'disposition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'expenses': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'floorNumber': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fot': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'frontGround': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'garageCoverage': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gateType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'industrialRoofType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'largeGround': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lightness': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'orientation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Property']", 'unique': 'True', 'primary_key': 'True'}),
            'quantityAmbiences': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBathrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBedrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBuildingFloors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantityElevators': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityGarages': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityShips': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'roofHeight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'roofType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'suitableProfessional': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'unityType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'})
        },
        'core.land': {
            'Meta': {'object_name': 'Land', 'db_table': "'core_property_land'", '_ormbases': ['core.Property']},
            'commercialUsage': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'frontGround': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'largeGround': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Property']", 'unique': 'True', 'primary_key': 'True'})
        },
        'core.local': {
            'Meta': {'object_name': 'Local', 'db_table': "'core_property_local'", '_ormbases': ['core.Property']},
            'buildingStatus': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'disposition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'expenses': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lightness': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'orientation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Property']", 'unique': 'True', 'primary_key': 'True'}),
            'quantityBathrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityGarages': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'})
        },
        'core.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.City']", 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Country']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Region']", 'null': 'True'})
        },
        'core.office': {
            'Meta': {'object_name': 'Office', 'db_table': "'core_property_office'", '_ormbases': ['core.Property']},
            'apartmentsPerFloor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'buildingCategory': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingCondition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingStatus': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'disposition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'expenses': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'floorNumber': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'garageCoverage': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lightness': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'orientation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Property']", 'unique': 'True', 'primary_key': 'True'}),
            'quantityBathrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBuildingFloors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantityElevators': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityGarages': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'})
        },
        'core.operation': {
            'Meta': {'object_name': 'Operation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'operation': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.ph': {
            'Meta': {'object_name': 'Ph', 'db_table': "'core_property_ph'", '_ormbases': ['core.Property']},
            'apartmentsPerFloor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'buildingCategory': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingCondition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingStatus': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'commercialUsage': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'disposition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'expenses': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'floorNumber': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'garageCoverage': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lightness': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'orientation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Property']", 'unique': 'True', 'primary_key': 'True'}),
            'quantityAmbiences': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBathrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBedrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBuildingFloors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantityElevators': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityGarages': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'suitableProfessional': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'unityType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'})
        },
        'core.picture': {
            'Meta': {'object_name': 'Picture'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'pic'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Post']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'core.post': {
            'Meta': {'object_name': 'Post'},
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'post_agent'", 'null': 'True', 'to': "orm['auth.User']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Category']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.City']", 'null': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Currency']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Operation']"}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'property': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Property']", 'unique': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Region']", 'null': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'post_user'", 'to': "orm['auth.User']"})
        },
        'core.property': {
            'Meta': {'object_name': 'Property'},
            'ambiences': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Ambience']", 'symmetrical': 'False', 'blank': 'True'}),
            'antiqueness': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Category']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Feature']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Location']", 'unique': 'True'}),
            'providesFunding': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Service']", 'symmetrical': 'False', 'blank': 'True'}),
            'square_meters': ('django.db.models.fields.FloatField', [], {}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.SubCategory']", 'null': 'True'}),
            'suitableCredit': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'total_meters': ('django.db.models.fields.FloatField', [], {}),
            'total_uncovered_meters': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'core.savedquery': {
            'Meta': {'object_name': 'SavedQuery', 'db_table': "'core_saved_query'"},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'query': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'core.service': {
            'Meta': {'object_name': 'Service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.shed': {
            'Meta': {'object_name': 'Shed', 'db_table': "'core_property_shed'", '_ormbases': ['core.Property']},
            'apartmentsPerFloor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'buildingCategory': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingCondition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingStatus': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'commercialUsage': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'disposition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'expenses': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'floorNumber': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fot': ('django.db.models.fields.IntegerField', [], {}),
            'frontGround': ('django.db.models.fields.IntegerField', [], {}),
            'garageCoverage': ('django.db.models.fields.IntegerField', [], {}),
            'gateType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'industrialRoofType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'largeGround': ('django.db.models.fields.IntegerField', [], {}),
            'lightness': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'orientation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Property']", 'unique': 'True', 'primary_key': 'True'}),
            'quantityAmbiences': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBathrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBedrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBuildingFloors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantityElevators': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityGarages': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityShips': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'roofHeight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'roofType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'suitableProfessional': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'unityType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'})
        },
        'core.storage': {
            'Meta': {'object_name': 'Storage', 'db_table': "'core_property_storage'", '_ormbases': ['core.Property']},
            'apartmentsPerFloor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'buildingCategory': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingCondition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingStatus': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'buildingType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'commercialUsage': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'disposition': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'expenses': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'floorNumber': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fot': ('django.db.models.fields.FloatField', [], {}),
            'frontGround': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'garageCoverage': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gateType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'industrialRoofType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'largeGround': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lightness': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'orientation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Property']", 'unique': 'True', 'primary_key': 'True'}),
            'quantityAmbiences': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBathrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBedrooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityBuildingFloors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantityElevators': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityGarages': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'quantityShips': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'roofHeight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'roofType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'suitableProfessional': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'unityType': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'})
        },
        'core.subcategory': {
            'Meta': {'object_name': 'SubCategory', 'db_table': "'core_sub_category'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.userprofile': {
            'Meta': {'object_name': 'UserProfile', 'db_table': "'core_user_profile'"},
            'phone': ('django.db.models.fields.TextField', [], {'max_length': '40'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['core']