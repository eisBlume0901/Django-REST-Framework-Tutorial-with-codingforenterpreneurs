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

# endpoint2 = "http://localhost:8000/api/"
# response2 = requests.get(endpoint2)
# print(response2.status_code) # 200
# print(response2.headers) # Will return metadata about the request such as content type=application/json, server=WSGIServer/0.2 CPython/3.10.0, etc.
# # print(response2.json()) # Will return a random product from the database in JSON format
# print(response2.text) # Since we return a HttpResponse instead of JsonResponse, we will get the data in text format which is titlecontentprice

# endpoint3 = "http://localhost:8000/api/"
# response3 = requests.get(endpoint3)
# print(response3.status_code) # 200
# print(response3.headers)
# print(response3.json()) # Will return a random product from the database in JSON format
# {'title': 'Instant Pot Multi-Cooker', 'content': 'Cook meals faster with this versatile Instant Pot, combining multiple kitchen appliances into one for pressure cooking, slow cooking, and more.', 'price': 89.99, 'sale_price': '80.99'}

# endpoint4 = "http://localhost:8000/api/"
# response4 = requests.get(endpoint4)
# print(response4.status_code) # 200
# print(response4.headers)
# print(response4.json()) # Will return a random product from the database in JSON format
# {'title': 'Instant Pot Multi-Cooker', 'content': 'Cook meals faster with this versatile Instant Pot, combining multiple kitchen appliances into one for pressure cooking, slow cooking, and more.', 'price': '89.99', 'sale_price': '80.99'}
# Our serializer was able to serialize the data along with the sale_price field.

endpoint5 = "http://localhost:8000/api/add_product/"
response5 = requests.post(endpoint5, data={
    "title": "Wireless Charging Pad",
    "content": "Charge your smartphone effortlessly with this sleek wireless charging pad, compatible with most devices",
    "price": 29.99}) # W
print(response5.status_code) # 201
print(response5.headers)
print(response5.json()) # Will return the newly created product in JSON format
# {'title': 'Wireless Charging Pad', 'content': 'Charge your smartphone effortlessly with this sleek wireless charging pad, compatible with most devices', 'price': '29.99'}
