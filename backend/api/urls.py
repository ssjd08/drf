from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'
urlpatterns = [
    path("", views.api_home, name="api_home"),
    path("auth/", obtain_auth_token)
]

