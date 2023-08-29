# from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Product
import json
@api_view(["GET","POST"])
def hellow(request):
    http_request=request.method
    if http_request=="GET":
        # data=request.body
        # echo_data=json.loads(data)
        qs=Product.objects.all()
        data=ProductSerializer(qs,many=True).data
        # data.append(echo_data)
        return Response(data)
    if http_request=="POST":
        data = request.data
        serializer=ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        message={"provided":"invalid data"}
        return Response(message,status=400)


