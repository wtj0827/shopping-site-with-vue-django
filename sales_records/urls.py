from django.urls import path
from . import views


urlpatterns = [
    path('', views.saleinfo_list),
]