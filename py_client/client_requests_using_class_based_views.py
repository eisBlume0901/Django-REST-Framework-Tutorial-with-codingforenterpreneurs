import requests

pk = 2
endpoint1 = f"http://localhost:8000/api/products/{pk}/"
response1 = requests.get(endpoint1)
print(response1.status_code) # 200
print(response1.json()) # Must retrieve
# {'title': 'Wireless Bluetooth Headphones', 'content': 'Enjoy immersive sound quality with these stylish wireless Bluetooth headphones. Featuring noise cancellation, long battery life, and comfortable ear pads, they are perfect for music lovers and on-the-go professionals alike.', 'price': '79.99'}

# Commented this so it wont send the same request again since I forgot to set each product attributes to be unique
# endpoint2 = "http://localhost:8000/api/products/create/"
# data = {
#     'title': 'Smart LED Light Bulb',
#     'content': 'Control your lighting with this energy-efficient smart LED bulb. Compatible with voice assistants and mobile apps.',
#     'price': 19.99
# }
# response2 = requests.post(endpoint2, json=data)
# print(response2.status_code) # 201
# print(response2.json()) # Must retrieve
# {'title': 'Smart LED Light Bulb', 'content': 'Control your lighting with this energy-efficient smart LED bulb. Compatible with voice assistants and mobile apps.', 'price': '19.99'}

endpoint3 = "http://localhost:8000/api/products/create" # List all products since ListCreateAPIView is used (get and post)
response3 = requests.get(endpoint3)
print(response3.status_code) # 200
print(response3.json()) # Retrieves all products in the database