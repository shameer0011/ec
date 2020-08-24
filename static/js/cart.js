// it is included in 'main.html'..

var updateBtns = document.getElementsByClassName('update-cart');
for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productid:', productId, 'action:', action);

        console.log('User:', user);
        if (user === 'AnonymousUser') {
            console.log('user not login');
        }
        else {

            console.log('user authenticated');
            updateUserOrder(productId, action)

        }
    })
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
            location.reload()
        });
}

