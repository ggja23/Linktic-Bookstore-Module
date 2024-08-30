# -*- coding: utf-8 -*-


from odoo import models, fields

class LinkticBook(models.Model):
    _name = 'linktic.book'
    _description = 'Book'
    _rec_name = 'title'

    title = fields.Char(required=True)
    author_id = fields.Many2one('linktic.author', required=True, string="Author")
    published_date = fields.Date()
    isbn = fields.Char(string="ISBN")
    price = fields.Float(required=True)
    quantity_in_stock = fields.Integer(string="Quantity in Stock", default=0)
