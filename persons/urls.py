from django.urls import path
from . import views


urlpatterns = [
    path('seller/', views.seller_list),
    path('customer/', views.customer_list),
]