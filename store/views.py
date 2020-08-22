from django.shortcuts import render
from .models import Product,Order,Customer,OrderItem,ShippingAddress

# Create your views here.
def store(request):
    product=Product.objects.all()
    context={'product':product}
    return render(request,'store/store.html',context)

def cart(request):
    
        if request.user.is_authenticated:
            customer = request.user.customer#to get  customer name..
            print(customer)
            #User and Customer is oneToOne field..
            order, created = Order.objects.get_or_create(customer12=customer, complete=False)
            print(order)
            print(created)
            items = order.orderitem_set.all()
            print(items)
        else:
            #Create empty cart for now for non-logged in user
            items = []
            
        context = {'items':items,'order':order}
        return render(request, 'store/cart.html', context)

def checkout(request):
    context={}
    return render(request,'store/checkout.html',context)

def checkout1(request):
   
    return render(request,"checkout1.html")





