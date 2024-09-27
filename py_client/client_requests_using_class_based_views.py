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

# endpoint3 = "http://localhost:8000/api/products/create" # List all products since ListCreateAPIView is used (get and post)
# response3 = requests.get(endpoint3)
# print(response3.status_code) # 200
# print(response3.json()) # Retrieves all products in the database

# endpoint4 = "http://localhost:8000/api/products/11/update/" # Updated the product with existing primary key 11 using CreateAPIView
# data = {
#     'title': 'SmartHome Guardian 360',
#     'content': 'The SmartHome Guardian 360 is an AI-driven security system that offers 4K video resolution and smart alerts for real-time monitoring. Easily integrated with your smart home devices, it provides peace of mind from anywhere via a mobile app.',
#     'price': 249.99
# }
# response4 = requests.put(endpoint4, json=data)
# print(response4.status_code)
# print(response4.json())

# endpoint5 = "http://localhost:8000/api/products/12/update/" # Updated the product with existing primary key 12 using CreateAPIView
# data = {
#     'title': 'SmartPlant Watering System',
#     'content': 'The SmartPlant Watering System automates plant care by delivering precise amounts of water based on soil moisture levels. Connect via an app to monitor your plants’ needs from anywhere.',
#     'price': 89.99
# }
#
# response5 = requests.put(endpoint5, json=data)
# print(response5.status_code)
# print(response5.json())

# endpoint6 = "http://localhost:8000/api/products/14/delete/" # Deleted the product with existing primary key 14 using DeleteAPIView
# response6 = requests.delete(endpoint6)
# print(response6.status_code)
