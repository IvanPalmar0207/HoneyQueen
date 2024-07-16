from django.db import models
#Product Model
from Products.models import tb_products
#User Model
from Users.models import User
# Create your models here.

'''class tb_order(models.Model):
    orderId = models.AutoField(primary_key = True, verbose_name = 'Order Id')
    orderQuantity = models.IntegerField(verbose_name = 'Order Quantity')
    orderSize = models.CharField(max_length = 50, verbose_name = 'Order Size')
    productId = models.ForeignKey(tb_products, on_delete = models.CASCADE)
    documentNumber = models.ForeignKey(User, on_delete = mode)
'''