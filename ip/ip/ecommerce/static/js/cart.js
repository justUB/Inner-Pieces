
var updatebtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updatebtns.length; i++){
    updatebtns[i].addEventListener('click',function(){
        var itemName = this.dataset.prodname
        var action = this.dataset.action
        console.log('itemName: ', String(itemName))
        console.log('USER: ', user)
        if (user == 'AnonymousUser'){
            
            addcookieitem(itemName,action)
        }
        else{
            updateorder(itemName,action)
        }
    })
}

function addcookieitem(itemName,action){
    console.log('not logged in...')
    if (action=='add'){
        if (cart[itemName] == undefined){
            cart[itemName] = {'quantity':1}
        }
        else {
            cart[itemName]['quantity'] += 1 
        }
    }
    if (action=='remove'){
        cart[itemName]['quantity'] -= 1

        if(cart[itemName]['quantity']<=0){
            console.log('Delete item')
            delete cart[itemName]

        }
    }

    alert('Cart Modified')
    console.log('cart: ',cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}

function updateorder(itemName,action){
    console.log('logged in')

    var url = '/ecom/update_item/'
    
    fetch(url ,{
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'itemName':itemName,'action':action}),
    })
    
    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        alert('Cart Modified')
        location.reload()
    })
}