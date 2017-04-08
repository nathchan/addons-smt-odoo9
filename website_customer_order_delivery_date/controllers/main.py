# -*- coding: utf-8 -*-
# Part of BiztechCS. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from openerp import http
from openerp.http import request
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
from openerp.addons.website_sale.controllers.main import website_sale

class WebsiteSale(website_sale):

    """Add Customer Order Delivery functions to the website_sale controller."""

    @http.route(['/shop/customer_order_delivery'],
                type='json', auth="public", methods=['POST'], website=True)
    def customer_order_delivery(self, **post):
        """ Json method that used to add a
        delivery date and/or comment when the user clicks on 'pay now' button.
        """

        user_date_format = request.env['res.lang'].search(
            [('code', '=', str(request.context.get('lang', False)))]).date_format

        if post.get('delivery_date') or post.get('delivery_comment'):
            sale_order_obj = request.env['sale.order'].sudo()
            order = request.website.sale_get_order(context=request.context)
            redirection = self.checkout_redirection(order)
            if redirection:
                return redirection

            if order and order.id:
                values = {}
                if post.get('delivery_comment'):
                    values.update(
                        {'customer_order_delivery_comment': post.get('delivery_comment')})
                else:
                    values.update(
                        {'customer_order_delivery_comment': 'No Comment'})


                p_date = datetime.strptime(post.get('delivery_date'), '%m/%d/%Y')

                post_date = datetime.strftime(p_date, '%m/%d/%Y')#str(user_date_format))

                today_date = datetime.strftime(datetime.today(), '%m/%d/%Y')#user_date_format)


                # p_date = datetime.strptime(post.get('delivery_date'), DEFAULT_SERVER_DATE_FORMAT)

                # post_date = datetime.strftime(p_date, DEFAULT_SERVER_DATE_FORMAT)

                # today_date = datetime.strftime(datetime.today(), DEFAULT_SERVER_DATE_FORMAT)

                if post_date >= today_date:
                    values.update({
                        'customer_order_delivery_date': post.get('delivery_date')
                        })

                order.write(values)

        return True
