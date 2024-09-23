from rest_framework import generics # Using class based views instead of using api_view decorator methods
from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer # Automatically serializes the data into JSON
    lookup_field = 'pk' # The field that we want to use to look up the object
    # For customized queryset
    # def get_queryset(self):
    #     return Products.objects.filter(id=self.kwargs['id'])

