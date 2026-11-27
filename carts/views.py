from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product
from carts.models import Cart, CartItem
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import CartItem
from .serializers import CartItemSerializer, AddToCartSerializer, RemoveFromCartSerializer, AddOrSubstractFromCartSerializer
from rest_framework import status, serializers


# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def cart(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    serializer = CartItemSerializer(cart_items, many=True)
    return JsonResponse({
        "message": serializer.data 
    })

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_items_to_cart(request):
    serializer = AddToCartSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    cart, created = Cart.objects.get_or_create(user=request.user)
    product = serializer.validated_data["product"]
    quantity = serializer.validated_data["quantity"]

    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={"quantity": quantity}
    )
    
    if not item_created:
        cart_item.quantity += quantity
        cart_item.save(update_fields=["quantity"])
    
    return JsonResponse({
        "message": "Item successfully added",
        "item_id": cart_item.id,
        "quantity": cart_item.quantity
    }, status=status.HTTP_201_CREATED)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_items_from_cart(request):
    serializer = RemoveFromCartSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    cart = Cart.objects.get(user=request.user)
    product = serializer.validated_data["product"]

    cart_item = CartItem.objects.filter(
        cart = cart,
        product = product
    ).delete()

    return JsonResponse({
        "message": "Item successfully removed",
        "item_id": cart_item.id,
        "quantity": cart_item.quantity
        
    }, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_or_substract_item_quantity(request):
    serializer = AddOrSubstractFromCartSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    cart = Cart.objects.get(user=request.user)
   
    product = serializer.validated_data["product"]
    type = serializer.validated_data["type"]

    cart_item = CartItem.objects.get(
        cart = cart,
        product = product
    )

    if type == "add":
        cart_item.quantity += 1
    elif type == "substract":
        cart_item.quantity -= 1
    cart_item.save(update_fields=["quantity"])

    return JsonResponse({
        "message": "Item quantity successfully updated",
        "item_id": cart_item.id,
        "quantity": cart_item.quantity
    })

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def calculate_subtotal(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    subtotal = 0
    for item in cart_items:
        subtotal += item.product.price * item.quantity

    return JsonResponse({
        "message": "Subtotal successfully fetched",
        "subtotal": subtotal
    })
        
    
    

        
        
    