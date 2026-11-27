from rest_framework import serializers
from .models import CartItem
from products.models import Product

class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = "__all__"

class AddToCartSerializer(serializers.ModelSerializer):

    product_id = serializers.PrimaryKeyRelatedField(
        queryset = Product.objects.all(),
        source="product"
    )

    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = CartItem
        fields = ["product_id", "quantity"]