# -*- coding: utf-8 -*-


from odoo import models, fields

class LinkticCustomer(models.Model):
    _name = 'linktic.customer'
    _description = 'Customer'

    name = fields.Char(required=True)
    contact_details = fields.Text(string='Contact details')
    customer_since = fields.Date(default=fields.Date.today)
    purchase_ids = fields.One2many('linktic.sale.order', 'customer_id', string="Purchases")
