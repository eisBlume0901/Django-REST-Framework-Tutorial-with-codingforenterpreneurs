
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view # We are using api_view decorators instead of class-based API views
from products.serializers import ProductSerializer

#JsonResponse means that the response will be in JSON format.
# Create your views here.

# Instead of creating class based API views, method based API views are used which is overridden
# def api_home(request, *args, **kwargs):
#     data = {
#         "message": "Hello, World!", # For testing purposes.
#     }
#     return JsonResponse(data) # This will return the data in JSON format.

# def api_home(request, *args, **kwargs):
#     print(request.GET) # Retrieves params from the endpoint or params set from request.get() method. In this case, it is <QueryDict: {'company': ['I Azure You']}>
#     print(request.POST) # Retrieves json from the endpoint or json set from request.get() method. In this case, it is {'name': 'Eisblume', 'job': 'Software Engineer'}
#     body = request.body # request.body is a string of JSON data.
#     data = {}
#     try:
          # serialize - converting models into JSON format
          # deserialize - converting JSON format into models
#         data = json.loads(body) # convert JSON string data into a dictionary.
#         # For now, data is empty since we are not sending any data in the request.
#     except json.JSONDecodeError:
#         pass
#     print(data)
#     print(data.keys)
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers) # request.headers is a dictionary of headers. It contains metadata about the request.
#     data['content_type'] = request.content_type # request.content_type is the content type of the request. It is text/plain in this case
#     print(data)
#     return JsonResponse(data)
# {'name': 'Eisblume', 'job': 'Software Engineer', 'params': <QueryDict: {'company': ['I Azure You']}>, 'headers': {'Content-Length': '48', 'Content-Type': 'application/json', 'Host': 'localhost:8000', 'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}, 'content_type': 'application/json'}

@api_view(['GET']) # Adding the HTTP verb restricts the view to only accept GET requests.
def api_home(request, *args, **kwargs):
    # model_data = Product.objects.all().order_by("?").first() # Get a random product from the database. Question Mark (?) is used to get a random object.
    # data = {}
    # Instead of manually setting the data dictionary keys and parameters,
    # which is time-consuming and error-prone, we can use serializers
    # to convert the model data into JSON format.

    # Version 1
    # if model_data:
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price

    # Version 2
    # if model_data:
    #     data = model_to_dict(model_data, fields=['title', 'content', 'price'])
    # return JsonResponse(data)

    # Version 3 but this one converts json file into a string
    # if model_data:
    #     data = model_to_dict(model_data, fields=['title', 'content', 'price'])
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={'Content-Type': 'application/json'}) # This will return the data in JSON format.

    # if model_data:
    #     data = model_to_dict(model_data, fields=['title', 'content', 'price','sale_price']) #Since sale_price was not able to be serialized, we have to manually set it
    #     data['sale_price'] = model_data.sale_price
    #     return Response(data)

    # Version 4 Use a Django REST Framework
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)

