import requests

# #localhost = 127.0.0.1
# endpoint = "http://localhost:8000/api" # I am using the Django server to test the client requests.
#
# response = requests.get(endpoint)
# print(response.status_code) # 200 since we activated the server through python manage.py runserver
# print(response.text) # Retrieve the html page in text format (default html page of Django not customized).
# # Since we customize the endpoint's view method is api_home, we will get the JsonResponse to be
# # "message": "Hello, World!" in JSON format.
#
# endpoint1 = "http://localhost:8000/api/"
# #endpoint1 = "http://localhost:8000/api?company=I Azure You" # Could also set the params directly to the endpoint
# response1 = requests.get(endpoint1, params={"company": "I Azure You"}, json={"name": "Eisblume", "job": "Software Engineer"})
# print(response1.status_code) # 200
# print(response1.json()) # Retrieve the html page in text format (default html page of Django not customized).

endpoint2 = "http://localhost:8000/api/"
response2 = requests.get(endpoint2)
print(response2.status_code) # 200
print(response2.headers) # Will return metadata about the request such as content type=application/json, server=WSGIServer/0.2 CPython/3.10.0, etc.
# print(response2.json()) # Will return a random product from the database in JSON format
print(response2.text) # Since we return a HttpResponse instead of JsonResponse, we will get the data in text format which is titlecontentprice

