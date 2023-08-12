from django.contrib import admin
<<<<<<< HEAD
from .models import *
=======
from .models import Category,Product, Cart
>>>>>>> fd114003eeaabb9755207492f08a3ce5aacd36a3

 

admin.site.register(Category)
admin.site.register(Product)
<<<<<<< HEAD
admin.site.register(Cart)

admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
=======
admin.site.register(Cart)
>>>>>>> fd114003eeaabb9755207492f08a3ce5aacd36a3
