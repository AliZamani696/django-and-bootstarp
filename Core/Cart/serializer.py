
from rest_framework import serializers
from .models import Cart,CartItem





class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.ProductName",read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "product", "product_name", "quantity", "total"]


class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["id", "items", "total_price"]