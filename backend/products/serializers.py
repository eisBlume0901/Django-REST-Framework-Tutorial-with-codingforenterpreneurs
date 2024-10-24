from rest_framework import serializers
from products.models import Product

# Can have multiple serializers for the same model as long as the
# class name is different

# Another feature of Serializer is to clean and validate the data
# before saving such as checking if the data is in the correct format and data type


# Serializers can also be multiple for one model (PrimaryProductSerializer, SecondaryProductSerializer)
class ProductSerializer(serializers.ModelSerializer):

    # For customized fields, we can use SerializerMethodField
    # read_only means that the field is read-only and cannot be modified by the user or client

    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ['title', 'content', 'price', 'sale_price', 'discount'] # Sale price and discount is not editable by the user or client

    # The method name must be the same as the field name that was created get_<field_name>
    def get_discount(self, obj):
        return obj.get_discount_of_ten_percent() # This is a method from the Product model

    # Using SerializerMethodField with read_only=True is useful
    # 1. Customization: allowing to define custom logic for field's value that is either a model or a serializer field
    # 2. Read-only: preventing the field from being used in the update or create operations, maintaining data integrity
    # 3. Dynamic: enabling the field to be updated based on the value of other fields in the serializer