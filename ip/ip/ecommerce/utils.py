import json
from .models import *
from users.models import User
def guestcart(request):
    try: 
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart={}

    print("cart: ", cart)
    items = [] 
    order={'total_bill':0,'total_quantity':0}
    cart_quantity = order['total_quantity']

    for i in cart:
        try: 
            cart_quantity += cart[i]['quantity']

            Item = item.objects.get(name=i)
            total = Item.price * cart[i]['quantity']

            order['total_bill'] += total
            order['total_quantity'] += cart[i]['quantity']
            
    
            Items = {
                'item':{
                    'category': Item.category,
                    'name': Item.name,
                    'price': Item.price,
                    'image': Item.image,
                },
                'quantity': cart[i]['quantity'],
                'total_price': total,
            }

            items.append(Items)
        except:
            pass

    return {'items':items,'order':order,'cart_quantity':cart_quantity}

def cartData(request):
    if request.user.is_authenticated:
        user = request.user
        order,added = cart.objects.get_or_create(user = user,complete=False)
        items = order.cart_item_set.all()
        cart_quantity = order.total_quantity
    else:
        guestdata = guestcart(request)
        items = guestdata['items']
        order = guestdata['order']
        cart_quantity = guestdata['cart_quantity']

    return {'items':items,'order':order,'cart_quantity':cart_quantity}

def guestobj(request,data):
    print('user is not logged in')
    print('Cookies:' ,request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']

    data = cartData(request)
    items = data['items']
    user,created = User.objects.get_or_create(email = email)
    user.username = name
    user.save()
    

    order,added = cart.objects.get_or_create(
        user = user,
        complete = False,
    )


    for i in items:
        Item = item.objects.get(name = i['item']['name'])

        c_item = cart_item.objects.create(
            item = Item,
            order = order,
            quantity = i['quantity']
        )

    return user,order