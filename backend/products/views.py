from rest_framework import generics # Using class based views instead of using api_view decorator methods
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 # This is used to get a single object from the database and return a 404 error if the object does not exist

# Types of API Views
# 1. ListAPIView - To list all the objects in the database
# 2. RetrieveAPIView - To retrieve a single object from the database
# 3. CreateAPIView - To create a new object in the database
# 4. DestroyAPIView - To delete an object from the database
# 5. UpdateAPIView - To update an object in the database
# 6. ListCreateAPIView - To list all the objects in the database and create a new object in the database
# 7. RetrieveUpdateAPIView - To retrieve a single object from the database and update the object
# 8. RetrieveDestroyAPIView - To retrieve a single object from the database and delete the object
# 9. RetrieveUpdateDestroyAPIView - To retrieve a single object from the database, update the object and delete the object

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer # Automatically serializes the data into JSON
    lookup_field = 'pk' # The field that we want to use to look up the object
    # For customized queryset
    # def get_queryset(self):
    #     return Products.objects.filter(id=self.kwargs['id'])

product_detail_view = ProductDetailAPIView.as_view()
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer): # To customize the save or create method, you can override the perform_create method
        # serializer.save(user=self.request.user) # This is to join the user to the product (this is a customized one)
        print(serializer.validated_data)
        print(f"title: {serializer.validated_data.get('title')}")
        content = serializer.validated_data.get('content')
        if content is None:
            print(f"content: {serializer.validated_data.get('content')}")
        else:
            print(f"content: {content}")
        print(f"price: {serializer.validated_data.get('price')}")
        serializer.save()
        # Django Signals - A way to trigger a function when a certain event occurs in mysql it is called triggers
        # For example, when a new product is created, we can send an email to the user who created the product
        # We can use the post_save signal to trigger the function

product_list_create_view = ProductListCreateAPIView.as_view()

# Method-based API views
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        # Retrieve a specific product or list all products
        # Detail View
        # Can use .filter(), .get(), or .get_object_or_404() to get a single object
        # Can Also use Response or Http404 to return the data
        if pk is not None:
            product = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(product).data # You can explicitly declare many = False but it is not necessary
            return Response(data, status=200)
        else:
        # List View
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data # many = true means that we are serializing multiple objects
            return Response(data, status=200)
    if method == "POST":
        # Create a product
        serializer = ProductSerializer(data=request.data) # This is to validate the data
        if serializer.is_valid(raise_exception=True): # This is to raise an exception if the data is invalid
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = None
            price = serializer.validated_data.get('price')
            product = Product.objects.create(title=title, content=content, price=price)
            data = ProductSerializer(product).data
            return Response(data, status=201)


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content: # If the content is empty, set it to None
            instance.content = None

product_update_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

product_delete_view = ProductDeleteAPIView.as_view()
