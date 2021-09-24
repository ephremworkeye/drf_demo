from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

## List, Retrive, Create, Update, Update partial and delete
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
