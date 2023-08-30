from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name="List_view"),
    path('create/', views.ProductListCreateAPIView.as_view(), name="create_view"),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name="Detail_view"),
    path('<int:pk>/destroy/', views.ProductDestroyAPIView.as_view(), name="Destroy_view"),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name="update_view"),
]