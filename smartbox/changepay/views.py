from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer

class ProductDetailAPIView(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    def get(self,request,*args,**kwargs):
        pk=kwargs.get("pk")
        print(pk)
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self, serializer):
        if serializer.is_valid(raise_exception=True):
            modifying_price=serializer.validated_data.get("price")
            price=1.1*float(modifying_price)
            serializer.save(price=price)

    def put(self,request,*args,**kwargs):
        # instance=self.get_object()
        # serializer=self.get_serializer(instance,data=request.data)
        # if serializer.is_valid(raise_exception=True):
        #     self.perform_update(serializer)
        #     return Response(serializer.data)
        return self.partial_update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)











