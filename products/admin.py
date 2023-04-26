from django.contrib import admin
from .models import Seller,Buyer,Address,Product,OrderProduct,Order

# Register your models here.
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)
