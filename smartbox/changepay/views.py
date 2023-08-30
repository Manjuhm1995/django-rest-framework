from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        content=serializer.validated_data.get("content")or None
        if content is None:
            content="this field shouldn't be empty"
        serializer.save(content=content)

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        content=serializer.validated_data.get("content")or None
        if content is None:
            content="this field shouldn't be empty"
        serializer.save(content=content)

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance=self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    # def perform_update(self, serializer):this is to update all field
    # def partial_update(self, request, *args, **kwargs):
    #     instance=self.get_object()
    #     serializer=self.get_serializer(instance,data=request.data,Partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     instance.content=serializer.validated_data.get("content")
    #     instance.save()
    #     return Response(serializer.data,status=status.HTTP_200_OK)

    # def perform_update(self, serializer):
    #     instance=self.get_object()
    #     print(instance.id)
    #     instance.content=serializer.validated_data.get("content")
    #     instance.save()
    #     serializer.save()
    #     return Response(serializer.data,status=status.HTTP_200_OK)
