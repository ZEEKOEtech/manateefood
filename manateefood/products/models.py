from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
#from users.models import House

class ProductCategory(models.Model):
    category_name = models.CharField(_("product name"), max_length=100, blank=False)

class Product(models.Model):
    product_name = models.CharField(_("product name"), max_length=100, blank=False)
    product_price = models.IntegerField(_("product price"), default=0, blank=False)

    #product_house = models.ForeignKey(House, on_delete=models.CASCADE)
    product_category = models.ForeignKey(ProductCategory, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(_("datetime created"), auto_now=True)
    updated_at = models.DateTimeField(_("datetime updated"), auto_now=True)
    deleted_at = models.DateTimeField(_("datetime deleted"), default=None)
