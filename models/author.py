# -*- coding: utf-8 -*-

from odoo import models, fields

class LinkticAuthor(models.Model):
    _name = 'linktic.author'
    _description = 'Author'

    name = fields.Char(string='name', required=True)
    biography = fields.Text(string='Biography')
    book_ids = fields.One2many('linktic.book', 'author_id', string="Books")
