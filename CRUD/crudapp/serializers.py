from rest_framework import serializers
from .models import *

class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrudModel
        fields = '__all__'