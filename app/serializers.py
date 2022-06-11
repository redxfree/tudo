from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class Commodityseraializer(serializers.ModelSerializer):
	class Meta:
		model  = Commodity
		fields = '__all__'
  
		def create(self,validated_data):
			commodity = Commodity.objects.create(name = validated_data ['name'],description = validated_data['description'],minimum_order_quantity = validated_data['minimum_order_quantity'],todays_price = validated_data ['todays_price'],offer_price = validated_data['offer_price'],measuring_unit = validated_data['measuring_unit'],discounted_price = validated_data ['discounted_price'],bulk_price = validated_data ['bulk_price'],bulk_qty = validated_data ['bulk_qty'],available_quantity = validated_data ['available_quantity'], min_available_qty = validated_data['min_available_qty'],max_available_qty = validated_data['max_available_qty'],max_qty_allowed_per_order = validated_data ['max_qty_allowed_per_order'], gst = validated_data ['gst'], isActive = validated_data [' isActive'],quantityPerCrate = validated_data['quantityPerCrate'],delivery_charge = validated_data['delivery_charge'],packingByCrateOrBag = validated_data['packingByCrateOrBag'],created = validated_data['created'],updated = validated_data['updated'])
			return commodity
		
class Activeserializer(serializers.ModelSerializer):
	class Meta:
		model  = User
		fields  = ('isActive','firstName')


