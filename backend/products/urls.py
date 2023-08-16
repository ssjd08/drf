from django.urls import path
from . import views 


urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name="List-Create-Product"),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name="Detail-Product"),
    path('destroy/<int:pk>/', views.ProductDestroyAPIView.as_view(), name="destroy-Product"),
    path('update/<int:pk>/', views.ProductUpdateAPIView.as_view(), name="update-Product"),
]
