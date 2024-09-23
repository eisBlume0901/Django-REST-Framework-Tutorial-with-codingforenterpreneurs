Under Django-REST-Framework-Tutorial-with-codingforenterpreneurs

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

Notes:

Class-based API Views under an app vs Method-based API Views with api_view decorators under api app
CLass-based API Views under an app
- Reusability - through inheritance and mixins
- Customization - easier to customize and extend the overriding methods
- Readability - readable and organized, especially for complex views
- Built-in Methods - provides built-in methods for common actions such as get, post, put, delete
- DRY Principle - reducing code duplication

Method-based API views with api_view decorators under api app
- Simplicity - simple and easy to understand
- Explicitness - more explicit in terms of HTTP methods being handled
- Quick Setup - Faster to setup for small projects or simple endpoints
- Less Overhead - Since there is no need to define a class
- Direct Control - provides direct control over the request handling process, which can be useful for straightforward logic
