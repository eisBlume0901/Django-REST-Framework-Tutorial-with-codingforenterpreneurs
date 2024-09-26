from rest_framework import generics # Using class based views instead of using api_view decorator methods
from .models import Product
from .serializers import ProductSerializer

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
