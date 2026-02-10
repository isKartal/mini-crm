from rest_framework import serializers
from .models import Customer, Deal

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'address', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at']

class DealSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Deal
        fields = ['id', 'customer', 'customer_name', 'title', 'amount', 'status', 'status_display', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at']
