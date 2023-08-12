from django.contrib import admin

from .models import *

from .models import Category,Product, Cart


 

admin.site.register(Category)
admin.site.register(Product)

admin.site.register(Cart)

admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)

