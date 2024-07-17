import uuid
from django.db import models
#Product Model
from Products.models import tb_products
#User Model
from Users.models import User
#Size Model
from Products.models import tb_sizes

class tb_cart(models.Model):
    cartId = models.UUIDField(default = uuid.uuid4, primary_key = True, verbose_name = 'Cart Id')
    cartUser = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Cart User')
    cartTotalValue = models.FloatField(null = True, verbose_name = 'Total Cart')
    cartCompleted = models.BooleanField(default = False, verbose_name = 'Cart Completed')

class tb_cartItem(models.Model):
    cartProduct = models.ForeignKey(tb_products, on_delete = models.CASCADE, verbose_name = 'Cart Product')
    cartId = models.ForeignKey(tb_cart, on_delete = models.CASCADE, verbose_name = 'Cart Id')
    cartQuantity = models.IntegerField(default = 0)
    cartSize = models.ForeignKey(tb_sizes, on_delete = models.CASCADE, verbose_name = 'Cart Size')