from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *

import razorpay
client = razorpay.Client(auth=("rzp_test_hepZ4mRxThxB1q", "nEo0pUYjlMLJvTFBNis6Pn90"))

client.set_app_details({"title" : "Learning", "version" : "1.8"})


# Create your views here.
def home(request):
    obj = product.objects.all()
    return render(request,'home.html',{'obj': obj})

def cart_products(request,user_id):
    all_products = cart.objects.filter(cust_id = user_id)
    ids = []
    for i in all_products:
        ids.append(i.product_id)
    product_list = product.objects.filter(p_id__in=ids)
    total = 0
    for j in product_list:
        total = total + j.price
    return render(request,'cart.html',{'product_list': product_list,'total':total})

def product_detail(request,p_id):
    obj = product.objects.get(p_id=p_id)
    return render(request,'product.html',{'obj': obj})

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def tocart(request):
    cust_id = request.POST.get('cust_id')
    product_id = request.POST.get('product_id')
    cart_products = cart.objects.create(cust_id=cust_id,product_id=product_id)
    cart_products.save()
    data = {
        'cust_id':cust_id,
        'product_id':product_id
    }
    return JsonResponse(data)

@csrf_exempt
def remove(request):
    product_remove_id = request.POST.get('p_id')
    a = cart.objects.filter(cust_id=1,product_id=product_remove_id)
    a.delete()
    data = {
        'message':"Product removed succesfully",
    }
    return JsonResponse(data)
