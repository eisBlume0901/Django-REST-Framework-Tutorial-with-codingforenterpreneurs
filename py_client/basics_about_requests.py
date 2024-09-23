import requests

#Endpoint is a URL used by the client to perform a request from the server.
#This request can be a GET, POST, PUT, DELETE, etc.
endpoint1 = "https://httpbin.org/status/200"
endpoint2 = "https://httpbin.org/anything" #This is a public API that returns the request data in JSON format.

response1 = requests.get(endpoint1) # This is an API method from httpbin.org call to the server to perform a GET request.
print(response1.status_code)
print(response1) # This will print the status code of the response from the server.
print(response1.text) # This will print the response data in text format but in this case there is no data to print.

response2 = requests.get(endpoint2)
print(response2.status_code)
print(response2.text) # This will print the response data in text format in dictionary format.
print(response2.json()) # This will print the response data in JSON format.

#HTTP requests returns HTML data which is what we known as web pages.
#API requests returns JSON data which is what we known as API responses (this JSON data can be used to create web pages).
#JSON data is metadata, it is data about data (metadata of a web page are the tags, attributes, etc).

response3 = requests.get(endpoint2, json={"name": "Eisblume", "job": "Software Engineer"})
print(response3.status_code)
print(response3.text) #
print(response3.json()) # This will print the response data in JSON format including the json passed in the request.

# params = 'args': {'job': 'Software Engineer', 'name': 'Eisblume'},
# For GET requests, data is appended to the URL as query parameters.
# Data is appended to the URL as query parameters.
# Example: https://httpbin.org/anything?name=Eisblume&job=Software%20Engineer

# json = 'data': '{"name": "Eisblume", "job": "Software Engineer"}',
# For POST requests, data is sent in the body of the request as JSON.
# Data is sent in the body of the request as JSON.
# Example:
# {
#   "name": "Eisblume",
#   "job": "Software Engineer"
# }

# data = 'form': {'job': 'Software Engineer', 'name': 'Eisblume'},
# For PUT requests, data is sent in the body of the request as form data.
# Data is sent in the body of the request as form data.
# DjangoForms are used to create forms in Django which are used to create web pages.
# This form data is sent in the body of the request as form data.
