from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('categories/', views.category_list),
    path('', views.product_list),
    url('(?P<pk>[0-9]+)$', views.product_detail),
]

# url(r'^api/categories/$', shop_views.category_list),
# url(r'^api/products/$', shop_views.product_list),
# url(r'^api/products/(?P<pk>[0-9]+)$', shop_views.product_detail),