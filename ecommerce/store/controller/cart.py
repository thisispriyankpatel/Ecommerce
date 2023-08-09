from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from store.models import Product,Cart


def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if (product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status':"Product Already in Cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >=prod_qty:
                        Cart.objects.create(user=request.user, prod_id=prod_id, prod_qty=prod_qty)
                        return JsonResponse({'status':"Product Added Successfully"})
                    else:
                        return JsonResponse({'status':"Only"+ str(product_check.quantity)+ "Quantity availble"})
            
                 
                
                


            else:
                return JsonResponse({'status':"No such product found"})

        
        else:
            return JsonResponse({'status': "Login To Continue"})

    return redirect('/')


def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render(request,"store/cart.html", context)