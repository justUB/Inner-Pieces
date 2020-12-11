from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import address_form
from django.http import JsonResponse
from .utils import cartData,guestobj
import json,datetime

def store(request):
    items = item.objects.all()
    data = cartData(request)
    cart_quantity = data['cart_quantity']

    context={'items':items, 'cart_quantity':cart_quantity}

    return render(request, 'ecom.html', context)


def cart_page(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cart_quantity = data['cart_quantity']

    context={'items':items,'order':order,'cart_quantity':cart_quantity}
    return render(request,'cart.html', context)

def checkout(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cart_quantity = data['cart_quantity']

    context={'items':items,'order':order,'cart_quantity':cart_quantity}
    return render(request,'checkout.html', context)

def updateitem(request):
    data = json.loads(request.body)
    itemName = data['itemName']
    action = data['action']
    

    user = request.user
    Item = item.objects.get(name = itemName)
    order,added = cart.objects.get_or_create(user = user,complete=False)

    order_item,created = cart_item.objects.get_or_create(order = order, item = Item)

    if action == 'add':
        order_item.quantity = order_item.quantity + 1
    elif action == 'remove':
        order_item.quantity = order_item.quantity - 1

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added' , safe = False)

def processOrder(request):
    transactionId = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        user = request.user
        order,added = cart.objects.get_or_create(user = user,complete=False)

    else:
        user,order = guestobj(request,data)
        
    total = float(data['form']['total'])
    order.transaction_id = transactionId
    if total == order.total_bill:
        order.complete = True
    order.save()

    address.objects.create(
        user = user,
        order = order,
        address = data['shipping']['address'],
        city = data['shipping']['city'],
        state = data['shipping']['state'],
        pincode = data['shipping']['zipcode'],
    )

    return JsonResponse('Payment Complete', safe = False)