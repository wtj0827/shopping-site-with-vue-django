from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.CharField(max_length=13, help_text="Enter Stock Keeping Unit")
    category = models.CharField(max_length=200, help_text="Enter category name", null=True)
    factory = models.CharField(max_length=200, help_text="Enter factory name", null=True)
    country = models.CharField(max_length=200, help_text="Enter country name", null=True)
    image = models.ImageField(upload_to='products_img', null=True)
    description = models.TextField(help_text="Enter product description", null=True)
    review = models.TextField(help_text="Enter review", null=True)
    object = models.CharField(max_length=200, help_text="Enter object", null=True)
    color = models.CharField(max_length=200, help_text="Enter product color", null=True)
    discountRange = models.IntegerField(max_length=200, help_text="Enter product discountRange", null=True)

    buyPrice = models.DecimalField(decimal_places=2, max_digits=20, help_text="Enter product price per unit")
    sellPrice = models.DecimalField(decimal_places=2, max_digits=20, help_text="Enter product price per unit")

    unit = models.CharField(max_length=10, help_text="Enter product unit")
    quantity = models.DecimalField(decimal_places=1, max_digits=20, help_text="Enter quantity")

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Product.
        """
        return reverse('product-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.sku
