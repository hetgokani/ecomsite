from django.shortcuts import render,redirect
from .models import Products,Order
# Create your views here.

def index(request):
    product_objects = Products.objects.all()

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects= product_objects.filter(name__icontains=item_name)
    return render (request,'shop/index.html',{'product_objects':product_objects})

def checkout(request):
 
    if request.method == "POST":
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state =request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()
        return redirect('payment') 
    return render(request,'shop/checkout.html')

def payment(request):
    return render(request,'shop/payment.html')

def paymentdone(request):
    return render(request,'shop/paymentdone.html')