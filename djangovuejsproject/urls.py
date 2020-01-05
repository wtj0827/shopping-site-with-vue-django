"""djangovuejsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView

import myshop

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    path('api/products/', include('myshop.urls')),
    path('api/persons/', include('persons.urls')),
    path('api/sale-records/', include('sales_records.urls')),
    url(r'^(?:.*)/?$', TemplateView.as_view(template_name='index.html'), name='catchall')
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
#     url(r'^(?:.*)/?$', TemplateView.as_view(template_name='index.html'), name='catchall'),
#     url(r'^api/categories/$', shop_views.category_list),
#     url(r'^api/products/$', shop_views.product_list),
#     url(r'^api/products/(?P<pk>[0-9]+)$', shop_views.product_detail),
# ]
