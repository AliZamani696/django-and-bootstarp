from .models import Product,Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer
from rest_framework.generics import ListAPIView




class AllProductsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "allproducts.html"
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response({
            "category": category,
            "products": products,
            "products_json": serializer.data
        })

class CategoryView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "category.html"
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response({
            "category": category,
            "category_json": serializer.data
        })

class AboutView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "about.html"
    def get(self, request):
        return Response()
class ContactView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "contact.html"
    def get(self, request):
        return Response()

