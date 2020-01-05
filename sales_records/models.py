from django.db import models
from django.urls import reverse
from myshop.models import Product


class SaleInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=2, max_digits=20)
    buy_price = models.DecimalField(decimal_places=2, max_digits=20)
    customer = models.CharField(max_length=13)
    seller = models.CharField(max_length=13)
    sale_date = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     """
    #     Returns the url to access a particular instance of Product.
    #     """
    #     return reverse('product-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.seller

