from rest_framework import serializers
from .models import Product
from accounts.serializers import UserSerializer

class ProductSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'product_image', 'created_at', 'updated_at', 'created_by']