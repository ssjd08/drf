from django.urls import path
from . import views 


urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name="Detail-Product"),
    path('', views.ProductListCreateAPIView.as_view(), name="Create-Product"),
]
