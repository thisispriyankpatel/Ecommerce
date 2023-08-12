from django.urls import path
from . import views
<<<<<<< HEAD
from store.controller import authview, cart, Wishlist,checkout, order
=======
from store.controller import authview, cart
>>>>>>> fd114003eeaabb9755207492f08a3ce5aacd36a3

urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:slug>', views.collectionsview, name="collectionsview" ),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),

    path('register/', authview.register, name="register" ),
    path('login/', authview.loginpage, name="loginpage" ),
    path('logout/', authview.logoutpage, name="logout" ),

          
<<<<<<< HEAD
    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('cart',cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),

    path('wishlist', Wishlist.index, name= "wishlist"),
    path('add-to-wishlist', Wishlist.addtowishlist, name ="addtowishlist"),

    path('deletewishlistitem', Wishlist.deleteWishlistItem, name= "deleteWishlistItem"),

    path('checkout', checkout.index, name="checkout"),
    path('place-order', checkout.placeorder, name="placeorder"),
    path('my-orders',order.index, name="myorders"),
    path('view-order/<str:t_no>', order.vieworder, name="orderView")
                   

=======
    path('cart-to-cart', cart.addtocart, name="addtocart"),
    path('cart',cart.viewcart, name="cart")
>>>>>>> fd114003eeaabb9755207492f08a3ce5aacd36a3
]