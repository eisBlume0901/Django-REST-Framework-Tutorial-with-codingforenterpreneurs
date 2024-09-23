from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0) # 12345.67
    def __str__(self):
        return self.title

    @property # An attribute of the class that can be access with dot notation. It is treated as an attribute not a method.
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.9) # 90% of the original price.

