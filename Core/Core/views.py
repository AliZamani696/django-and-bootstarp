
from Store.models import Product,Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from Store.serializer import ProductSerializer, CategorySerializer
from rest_framework.generics import ListAPIView



class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
            "products": products,
            "products_json": serializer.data
        })
