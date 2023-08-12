from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from store.models import Product,Cart,Wishlist,Order,OrderItem
from django.contrib.auth.decorators import login_required 

def index(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request, "store/orders/index.html", context)


def vieworder(request, t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    OrderItems = OrderItem.objects.filter(order=order)
    context = {'order':order, 'OrderItems':OrderItems}
    return render(request, "store/orders/view.html", context)