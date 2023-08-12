from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from store.models import Product,Cart,Wishlist
from django.contrib.auth.decorators import login_required 


@login_required(login_url= 'loginpage')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request,'store/wishlist.html', context)


def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status:"Product Is already in wishlist'})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status:"Product added to wishlist'})
            else:
                return JsonResponse({'status:"No such Product found'})

        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect('/')        



def deleteWishlistItem(request):
    if request.method == 'POST':
       if request.user.is_authenticated:
          prod_id = int(request.POST.get('product_id'))
          if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
              cartitem = Wishlist.objects.get(product_id=prod_id, user=request.user)
              cartitem.delete()
              return JsonResponse({'status': "Deleted Successully"})
       else:
           return JsonResponse({'ststus': "Login to Continue"})
    return redirect('/')