from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem, Cart
from Store.models import Product
from rest_framework.renderers import TemplateHTMLRenderer



class AddToCartAPIView(APIView):
    def post(self,request):
        user = request.user
        product_id = request.data.get("product_id")
        qty = int(request.data.get("quantity",1))
        product = Product.objects.filter(id=product_id).first()
        if not product:
            return Response({"error": "Product not found"}, status=404)
        cart, _ = Cart.objects.get_or_create(user=user)

        # If exists → update quantity
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )
        if not created:
            cart_item.quantity += qty
        cart_item.save()


        return Response({
            "message": "Added to cart"
            })


class CartView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "cart.html"
    def get(self,request):
        cartitems = CartItem.objects.all()
        print(cartitems)
        return Response({
            "cartitems":cartitems,
        })