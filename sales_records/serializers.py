
from rest_framework import serializers
from .models import SaleInfo


class SaleInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleInfo
        fields = '__all__'
