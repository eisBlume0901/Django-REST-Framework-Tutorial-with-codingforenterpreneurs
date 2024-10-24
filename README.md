Under Django-REST-Framework-Tutorial-with-codingforenterpreneurs

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

Notes:

Class-based (Generics) API Views under an app vs Method-based API Views with api_view decorators under api app vs Mixins API Views

### Class-based API Views under an app
- **Reusability**: Through inheritance and mixins.
- **Customization**: Easier to customize and extend by overriding methods.
- **Readability**: More readable and organized, especially for complex views.
- **Built-in Methods**: Provides built-in methods for common actions such as get, post, put, delete.
- **DRY Principle**: Reduces code duplication.

### Method-based API views with api_view decorators under api app
- **Simplicity**: Simple and easy to understand.
- **Explicitness**: More explicit in terms of HTTP methods being handled.
- **Quick Setup**: Faster to set up for small projects or simple endpoints.
- **Less Overhead**: No need to define a class.
- **Direct Control**: Provides direct control over the request handling process, useful for straightforward logic.

### Mixins API views
- **Reusability**: Reuse common functionality across multiple views.
- **Customization**: Easily customize behavior by overriding methods in the mixin.
- **Modularity**: Breaking down functionality into smaller, manageable pieces.
- **DRY Principle**: Helps in reducing code duplication by encapsulating common behavior.


Class-based API Views

Use for complex views requiring multiple HTTP methods and organized structure. Ideal for reusability and customization through inheritance and built-in methods.  


api_view Decorators

Use for simple, explicit setups with direct control over request handling. Best for quick setups and straightforward logic without class overhead.  


Mixins

Use for modular design and reusability of common functionality across views. Ideal for reducing code duplication and easy customization by overriding methods.

Generic Views: Used directly to create views that follow common patterns. 

Mixins: Used to extend or modify the behavior of other views

load vs loads vs dump vs dumps
- `load`: Reads JSON data from a file-like object and deserializes it into a Python object.

- `loads`: Deserializes a JSON-formatted string into a Python object.

- `dump`: Serializes a Python object and writes the JSON data to a file-like object.

- `dumps`: Serializes a Python object into a JSON-formatted string.


HttpResponse vs JsonResponse vs Response
- `HttpResponse`: use for simple text or HTML responses
    
- `JsonResponse`: use for JSON data without needing the full features of Django Rest Framework

- `Response`: use for more control over the response format, status codes, and content negotiation in Django Rest Framework