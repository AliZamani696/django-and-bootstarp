from django.db import models
from django.conf import settings
from Store.models import Product


# Create your models here.




class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    # def total_price(self):
    #     return sum(item.total() for item in self.items.all())

    # def __str__(self):
    #     return self.id



class CartItem(models.Model):
    cart = models.ForeignKey(Cart,related_name="items",on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def total(self):
        return self.product.ProductPrice * self.quantity

    class Meta:
        unique_together = ("cart","product")

