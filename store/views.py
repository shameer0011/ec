from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
#from .models import Product,Order,Customer,OrderItem,ShippingAddress
from .models import *

# Create your views here.
def store(request):
    # show total cart items..
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer12=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items=order.get_cart_items
    else:
        order={'get_cart_items':0,'shipping':False}
        cart_items=order['get_cart_items']
        print(cart_items)

    product=Product.objects.all()
    context={'product':product,'order':order,'cart_items':cart_items}
    return render(request,'store/store.html',context)

def cart(request):
    
        if request.user.is_authenticated:
            customer = request.user.customer#to get  customer name..
            print(customer)
            #User and Customer is oneToOne field..
            order, created = Order.objects.get_or_create(customer12=customer, complete=False)
            print(order)
            print(order.id)
            print(order.transaction_id)
            print(created)
            items = order.orderitem_set.all()
            cart_items=order.get_cart_items
            cart_total=order.get_cart_total
          
        else:
            #Create empty cart for now for non-logged in user
            items = []
            order={'get_cart_items':0,'get_cart_total':0,'shipping':False}
            cart_items=order['get_cart_items']
            cart_total=order['get_cart_total']
        
        context = {'items':items,'order':order,'cart_items':cart_items,'cart_total':cart_total}
        return render(request, 'store/cart.html', context)

def checkout(request):
       if request.user.is_authenticated:
            customer = request.user.customer#to get  customer name..
            #print(customer)
            #User and Customer is oneToOne field..
            order, created = Order.objects.get_or_create(customer12=customer, complete=False)
            #print(order)..show id of Order table..
            print(created)
            print(order.transaction_id)
            print(order.customer12)
            items = order.orderitem_set.all()
            print(items)
            cart_items=order.get_cart_items
            cart_total=order.get_cart_total
          
       else:
            #Create empty cart for now for non-logged in user
            items = []
            order={'get_cart_items':0,'get_cart_total':0,'shipping':False}
            cart_items=order['get_cart_items']
            cart_total=order['get_cart_total']
            
       context = {'items':items,'order':order,'cart_items':cart_items,'cart_total':cart_total}
       return render(request,'store/checkout.html',context)

def updateItem(request):
        data=json.loads(request.body)
        productId=data['pro_id']
        action=data['action_status']

        # print("Action:",action)
        # print("productId:",productId)
        customer=request.user.customer
        product=Product.objects.get(id=productId)
        print(product)#show only product's table forignkey..
        order, created = Order.objects.get_or_create(customer12=customer, complete=False)
        orderitems,created=OrderItem.objects.get_or_create(product=product, order=order)
        print(created)
        #print(orderitems)..all in 'orderitems'..so called 'orderitems.quantity,product.name..etc'..
        # l=orderitems.quantity
        # print("hai",l)
        # l=orderitems.quantity=orderitems.quantity+1
        # print("hai",l)
        if action=="add":
            orderitems.quantity= orderitems.quantity+1
        elif action=="remove":
            orderitems.quantity= orderitems.quantity-1
        orderitems.save()

        if  orderitems.quantity <= 0:
            orderitems.delete()

        return JsonResponse('item was added',safe=False)

def processOrder(request):
    #print('Data:haii...',request.body)
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)

    if request.user.is_authenticated:
            customer=request.user.customer
            order, created = Order.objects.get_or_create(customer12=customer, complete=False)
            print("pls.",order)
            order.transaction_id=transaction_id
            print(order.transaction_id)
            total=float(data['form12']['total'])
            if total==order.get_cart_total:
                order.complete=True
            order.save()
            #'shippingss'is a function in models.py..
            if order.shippingss==True:
                ShippingAddress.objects.get_or_create(customer=customer,order=order ,
                address=data['shipping12']['address'],
                state=data['shipping12']['state'],
                city=data['shipping12']['city'],
                zipcode=data['shipping12']['zipcode'])
    else:
        print("User not login")
    return JsonResponse('payment completed',safe=False)

def checkout1(request):
   
    return render(request,"checkout1.html")





