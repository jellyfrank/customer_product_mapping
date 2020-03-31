#!/usr/bin/python3
# @Time    : 2020-03-28
# @Author  : Kevin Kong (kfx2007@163.com)

from odoo import api, fields, models, _


class product_customer_info(models.Model):

    _name = "product.customer.info"

    name = fields.Many2one("res.partner", "Customer", domain=[
                           ('customer_rank', '>', 1)])
    product_name = fields.Char("Customer Product Name")
    product_variant = fields.Char("Customer Product Variant")
    product_code = fields.Char("Customer Product Code")
    product_id = fields.Many2one("product.template", "Product")


class product_template(models.Model):

    _inherit = "product.template"

    customer_ids = fields.One2many(
        "product.customer.info", 'product_id', string="Customers")


# class sale_order(models.Model):

#     _inherit = "sale.order"

