


from rest_framework import serializers

from .models import Product,Category



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = [
                "ProductQuantity",
                "ProductPrice",        
                "ProductSale"
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
         "CategoryName"
        ]
        read_only_fields = [
            "CategoryParent"
        ]