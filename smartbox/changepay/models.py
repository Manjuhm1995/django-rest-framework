from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default=None, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=100)

    def __str__(self):
        return self.title

    @property
    def get_title(self):
        return self.title+" "+"shubhavaagali"

    def discount_price(self):
        return float(self.price)*0.2

