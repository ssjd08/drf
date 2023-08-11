from django.urls import path
from . import views 


urlpatterns = [
    path('', views.ProdoctMixinAPIView.as_view(), name="List-Create-Product"),
    path('<int:pk>/', views.ProdoctMixinAPIView.as_view(), name="Detail-Product"),
    path('destroy/<int:pk>/', views.ProdoctMixinAPIView.as_view(), name="destroy-Product"),
    path('update/<int:pk>/', views.ProdoctMixinAPIView.as_view(), name="update-Product"),
]
