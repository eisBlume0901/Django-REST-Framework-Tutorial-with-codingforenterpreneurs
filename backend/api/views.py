from django.shortcuts import render
from django.http import JsonResponse
import json
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