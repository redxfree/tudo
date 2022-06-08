from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class Commodityseraializer(serializers.ModelSerializer):
    class Meta:
        model  = Commodity
        fields = '__all__'
        
class Activeserializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields  = ('isActive','firstName')
        