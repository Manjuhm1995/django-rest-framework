from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    discounted_price=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product
        fields=["id","title","content","price","get_title","discounted_price"]

    def get_discounted_price(self,obj):
        return obj.discount_price()