# -*- coding: utf-8 -*-
# Part of BiztechCS. See LICENSE file for full copyright and licensing details.

{
    "name" : "Customer Order Delivery Date",
    "author" : "BiztechCS",
    "version": "9.0.1.0.0",
    "category" : "Website",
    "website" : "http://www.biztechconsultancy.com",
    # 'license': 'Odoo Proprietary License v1.0',
    "description": "This module is used for add customer order delivery date section at payment page",
    "summary" : "Know when your customers want products delivered",
    "depends" : ['sale','website_sale'],
    "data":[
            'views/customer_order_delivery_config_view.xml',
            'views/sale_order_view.xml',
            'views/template.xml',
    ],
    'images': ['static/description/order-delivery-date-comments-profile.png'],
    # 'price': 10.00,
    # 'currency': 'EUR',
    'installable': True,
    'auto_install': False,
}
