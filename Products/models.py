from django.db import models

# Create your models here.

class tb_categories(models.Model):
    categoryId = models.AutoField(primary_key = True, verbose_name = 'Category Id')
    categorieName = models.CharField(max_length = 80, verbose_name = 'Category Name')

    def __str__(self):
        return f'{self.categorieName}'

class tb_referencies(models.Model):
    referenceId = models.AutoField(primary_key = True, verbose_name = 'Reference Id')
    referenceDescription = models.TextField(max_length = 80, verbose_name = 'Reference Description' )

    def __str__(self):
        return f'{self.referenceDescription}'

class tb_sizes(models.Model):
    sizeId = models.AutoField(primary_key = True, verbose_name = 'Size Id')
    sizeName = models.CharField(max_length = 30, verbose_name = 'Size Name')

    def __str__(self):
        return f'{self.sizeName}'

class tb_products(models.Model):
    productId = models.AutoField(primary_key = True, verbose_name = 'Product Id')
    productName = models.CharField(max_length = 80, verbose_name = 'Product Name')
    productDescription = models.TextField(max_length = 150, verbose_name = 'Product Description')
    productPrice = models.FloatField(verbose_name = 'Product Price')
    productStock = models.IntegerField(verbose_name = 'Product Stock', default = 1)
    productImage = models.ImageField(upload_to = 'media/', verbose_name = 'Product Image')
    categoryId = models.ForeignKey('tb_categories', verbose_name = 'Category Id', on_delete = models.CASCADE)
    referenceId = models.ForeignKey('tb_referencies', verbose_name = 'Reference Id', on_delete = models.CASCADE, blank = True, null = True, default = '')
    sizeId = models.ManyToManyField('tb_sizes', verbose_name = 'Size Id')

    def __str__(self):
        return f'{self.productName}'