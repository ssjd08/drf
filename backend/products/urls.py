from django.urls import path
from . import views 


urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name="product-list-create"),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name="product-detail"),
    path('destroy/<int:pk>/', views.ProductDestroyAPIView.as_view(), name="product-destroy"),
    path('update/<int:pk>/', views.ProductUpdateAPIView.as_view(), name="product-update"),
]
