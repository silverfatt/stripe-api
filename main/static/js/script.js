var buyButton = document.getElementById('buy-button');
var stripe = Stripe(buyButton.getAttribute('data-pk'));
buyButton.addEventListener('click', function () {
    var id = buyButton.getAttribute('data-id')
    url = '/buy/' + id
    fetch(url, {method: 'GET'}).then(function (response) {
        return response.json();
    }).then(function (data) {
        console.log(data);
        stripe.redirectToCheckout({sessionId: data.session_id})
    }).catch(function () {
        alert('The product is out of stock');
    });
});


