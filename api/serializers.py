from django.db.models import fields
from rest_framework import serializers
from .models import item

class itemSerializer(serializers.ModelSerializer):

    class Meta:
        model = item
        # fields= {'name', 'price'}
        fields = '__all__'