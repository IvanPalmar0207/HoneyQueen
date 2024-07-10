from django.contrib import admin

#Models
from Products.models import *

admin.site.register(tb_categories)
admin.site.register(tb_products)
admin.site.register(tb_referencies)
admin.site.register(tb_sizes)