# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class LinkticSaleOrderLine(models.Model):
    _name = 'linktic.sale.order.line'
    _description = 'Linktic Sale Order Line'

    sale_order_id = fields.Many2one('linktic.sale.order', string='Sale Order', required=True)
    book_id = fields.Many2one('linktic.book', string='Book', required=True)
    quantity = fields.Integer(string='Quantity', required=True, default=1)
    price = fields.Float(string='Price', required=True)
    total_price = fields.Float(string='Total Price', compute='_compute_total_price', store=True)
    returned_quantity = fields.Integer(string='Returned Quantity', default=0)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('returned', 'Returned'),
    ], string='State', default='draft')
    customer_id = fields.Many2one(related='sale_order_id.customer_id')

    @api.depends('quantity', 'price')
    @api.onchange('quantity', 'price')
    def _compute_total_price(self):
        for line in self:
            line.total_price = line.quantity * line.price


    @api.model
    def create(self, vals):
        book = self.book_id
        book.quantity_in_stock -= vals['quantity']
        return super(LinkticSaleOrderLine, self).create(vals)

    def unlink(self):
        book = self.book_id
        book.quantity_in_stock += self.quantity
        return super(LinkticSaleOrderLine, self).unlink()


    @api.constrains('returned_quantity')
    def _check_returned_quantity(self):
        for line in self:
            if line.returned_quantity > line.quantity:
                raise exceptions.ValidationError("Returned quantity cannot exceed the sold quantity.")

    def process_return(self, return_qty):
        for line in self:
            if line.state != 'confirmed':
                raise exceptions.UserError("Only confirmed orders can be returned.")
            if return_qty > line.quantity - line.returned_quantity:
                raise exceptions.UserError("Returned quantity exceeds available quantity.")
            line.returned_quantity += return_qty
            line.state = 'returned' if line.returned_quantity == line.quantity else 'confirmed'
            line.book_id.quantity_in_stock += return_qty
