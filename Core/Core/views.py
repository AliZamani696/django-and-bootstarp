
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
# views/error_views.py
from rest_framework.permissions import AllowAny

class NotFoundView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "404.html"

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'error': 'Endpoint not found',
                'message': 'The requested URL was not found on this server.',
                'status_code': status.HTTP_404_NOT_FOUND
            },
            status=status.HTTP_404_NOT_FOUND
        )

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)