// it is included in 'main.html'..but extended all html page..

var updateBtns = document.getElementsByClassName('update-cart');
console.log("haii", updateBtns.length)
for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productid:', productId, 'action:', action);

        console.log('User:', user);
        if (user === 'AnonymousUser') {
            //console.log('user not login');
            addCookieItem(productId, action)
        }
        else {

            console.log('user authenticated');
            updateUserOrder(productId, action)

        }
    })
}
//for unassigned user..
function addCookieItem(productId, action) {
    console.log('User is not authenticated')

    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = { 'quantity_s': 1 }

        } else {
            cart[productId]['quantity_s'] += 1
        }
    }

    if (action == 'remove') {
        cart[productId]['quantity_s'] -= 1

        if (cart[productId]['quantity_s'] <= 0) {
            console.log('Item should be deleted')
            delete cart[productId];
        }
    }
    console.log('CART:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"


}


function updateUserOrder(productId, action) {
    console.log('User is authenticated, sending data...')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'pro_id': productId, 'action_status': action })
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('data:', data)

        });
}

