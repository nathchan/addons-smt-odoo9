odoo.define('website_customer_order_delivery_date.payment', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    $(document).ready(function() {

        try {
            $("#delivery_date").datepicker({
                minDate: new Date()
            });
        } catch (e) {}
        var $payment = $("#payment_method");
        $payment.on("click", 'button[type="submit"],button[name="submit"]', function(ev) {
            ev.preventDefault();
            ev.stopPropagation();
            var customer_order_delivery_date = $('#delivery_date').val();
            var customer_order_delivery_comment = $('#delivery_comment').val();
            console.log('-----js-----')
            ajax.jsonRpc('/shop/customer_order_delivery/', 'call', {
                'delivery_date': customer_order_delivery_date,
                'delivery_comment': customer_order_delivery_comment
            });
        });
    });

});