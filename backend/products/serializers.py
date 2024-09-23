from rest_framework import serializers
from products.models import Product

# Can have multiple serializers for the same model as long as the
# class name is different

# Another feature of Serializer is to clean and validate the data
# before saving such as checking if the data is in the correct format and data type

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'content', 'price']

    # The SerializerMethodField is used for custom fields that are not in the model.
    # The method name should be the same as the property name in the model.

