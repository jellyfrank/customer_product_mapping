# -*- coding: utf-8 -*-
# from odoo import http


# class CustomerProductMapping(http.Controller):
#     @http.route('/customer_product_mapping/customer_product_mapping/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_product_mapping/customer_product_mapping/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_product_mapping.listing', {
#             'root': '/customer_product_mapping/customer_product_mapping',
#             'objects': http.request.env['customer_product_mapping.customer_product_mapping'].search([]),
#         })

#     @http.route('/customer_product_mapping/customer_product_mapping/objects/<model("customer_product_mapping.customer_product_mapping"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_product_mapping.object', {
#             'object': obj
#         })
