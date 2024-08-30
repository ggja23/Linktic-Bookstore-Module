# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class LinkticSaleOrder(models.Model):
    _name = 'linktic.sale.order'
    _description = 'Linktic Sale Order'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "name"
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'Name should be  unique!')
    ]
    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: 'New')
    customer_id = fields.Many2one('linktic.customer', string='Customer', required=True)
    order_line_ids = fields.One2many('linktic.sale.order.line', 'sale_order_id', string='Order Lines', required=True)
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('returned', 'Returned'),
        ('cancelled', 'Cancelled'),
    ], string='State', default='draft')

    company_id = fields.Many2one(
        comodel_name='res.company',
        required=True, index=True,
        default=lambda self: self.env.company)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('linktic.sale.order') or 'New'
        return super(LinkticSaleOrder, self).create(vals)

    @api.depends('order_line_ids.total_price')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(line.total_price for line in order.order_line_ids)

    def confirm_order(self):
        for order in self:
            if order.state != 'draft':
                raise exceptions.UserError("Only draft orders can be confirmed.")
            order.state = 'confirmed'
            for line in order.order_line_ids:
                line.book_id.quantity_in_stock -= line.quantity

    def process_return(self, return_lines):
        for order in self:
            if order.state != 'confirmed':
                raise exceptions.UserError("Only confirmed orders can be returned.")
            for line, return_qty in return_lines.items():
                if line in order.order_line_ids:
                    line.process_return(return_qty)
            order.state = 'returned' if all(line.state == 'returned' for line in order.order_line_ids) else 'confirmed'

    @api.model
    def get_dashboard_data(self):
        """Return dashboard data"""
        company_id = self.env.company

        # Total Sales
        total_sales = self.search_count([('company_id', '=', company_id.id)])

        # Total Products Sold
        total_products_sold = sum(
            line.product_uom_qty for order in self.search([('company_id', '=', company_id.id)]) for line in
            order.order_line)


        # Stock Levels
        stock_levels = sum(self.env['linktic.sale.order.line'].search([]).mapped('quantity'))

        # Recent Sales
        recent_sales = len(self.search([('company_id', '=', company_id.id)], limit=5))

        return {
            'total_sales': total_sales,
            'total_products_sold': total_products_sold,
            'stock_levels': stock_levels,
            'recent_sales': recent_sales,
        }