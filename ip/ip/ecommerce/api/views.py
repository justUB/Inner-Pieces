from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from users.models import User
from ecommerce.models import *
from .serializers import ItemsSerializer,cartSerializer,cartItemSerializer
import json,datetime
from rest_framework.permissions import IsAuthenticated

@api_view(http_method_names=['GET','POST'])
@permission_classes([IsAuthenticated])
def api(request):
    if request.method == 'GET':
        return item_get(request)

    if request.method == 'POST':
        return item_post(request)

@api_view(http_method_names=['GET','POST'])
@permission_classes([IsAuthenticated])
def cart_view(request):
    if request.method == 'GET':
        return cart_get(request)
    
    elif request.method == 'POST':
        return cart_post(request)

@api_view(http_method_names=['GET','POST'])
@permission_classes([IsAuthenticated])
def checkout_view(request):
    if request.method == 'POST':
        return checkout_post(request)
    

def checkout_post(request):

    data = json.loads(request.body)
    username = data['username']
    email = data['email']

    user,created = User.objects.get_or_create(username = username,email = email)
    
    print(user,'chek cart get')    
    transactionId = datetime.datetime.now().timestamp()
    
    order,added = cart.objects.get_or_create(user = user,complete=False)
    order.transaction_id = transactionId
    order.complete = True
    order.save()

    serializer = cartSerializer(order)
    return Response(data=serializer.data)


def cart_get(request):
    
    try:

        data = json.loads(request.body)
        username = data['username']
        email = data['email']

        user,created = User.objects.get_or_create(username = username,email = email)

        c_data = cart.objects.get(user=user,complete=False)
        ci_data = cart_item.objects.filter(order=c_data)

        serializer = cartItemSerializer(ci_data,many=True)
        return Response(data=serializer.data)
    except:
        return Response(status=404)


@api_view(http_method_names=['GET',])
def order_get(request):

    try:

        data = json.loads(request.body)
        username = data['username']
        email = data['email']
        user,created = User.objects.get_or_create(username = username,email = email)
        
        c_data,created = cart.objects.get_or_create(user=user,complete=False)
        serializer = cartSerializer(c_data)
        return Response(data=serializer.data)
    except:
        return Response(status=404)


def cart_post(request): 

    data = json.loads(request.body)
    itemName = data['itemName']
    action = data['action']
    username = data['username']
    email = data['email']

    user,created = User.objects.get_or_create(username = username,email = email)

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
    
    order_item = cart_item.objects.filter(order = order)
    serializer = cartItemSerializer(order_item,many=True)
    return Response(data=serializer.data)

   
def item_get(request):
    try:
        i_data = item.objects.all()
        serializer = ItemsSerializer(i_data,many=True)
        return Response(data=serializer.data)
    except item.NotFound():
        return Response(status=status.HTTP_404_NOT_FOUND)


def item_post(request):
    pass