from django.shortcuts import render
from django.contrib import messages
from . models import *


def home(request):
    return render(request, "store/index.html")


def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request, "store/collections.html", context)


def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        conetext = {'products': products, 'category':category}
        return render(request, "store/products/index.html", conetext)
    else:
        messages.warning(request, "No Category Found")
        return redirect('collections')

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products':products}
                   


        else:
            messages.error(request, "No Product Found")
            return redirect('collections')


    else:
        messages.error(request, "No Category Found")
        return redirect('collections')

    return render(request, "store/products/view.html", context)