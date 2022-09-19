var buyButton = document.getElementById('buy-button');
var stripe = Stripe(buyButton.getAttribute('data-pk'));
buyButton.addEventListener('click', function () {
    fetch('/buy/' + buyButton.getAttribute('data-type') + '/' + buyButton.getAttribute('data-id'),
        {
            method: 'GET',
            type: buyButton.getAttribute('data-type'),
        }).then(function (response) {
        return response.json();
    }).then(function (data) {
        console.log(data);
        stripe.redirectToCheckout({sessionId: data.session_id})
    }).catch(function () {
        alert('The product is out of stock');
    });
});


