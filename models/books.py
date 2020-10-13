from odoo import fields, models


class Books(models.Model):
    _name = 'lib.books'
    _description = 'Books'
    _rec_name = 'book'

    book = fields.Char(string='Book Name', required=True)
    author = fields.Char(string='Authors', required=True)
    editor = fields.Char(string='Editors', required=True)
    year = fields.Char(string='Year of edition', required=True)
    isbn = fields.Char(string='ISBN', required=True)
    image = fields.Binary(string='image')

class Customer(models.Model):
    _name = "lib.customer"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "activity table"

    name = fields.Char(string='Name')
    email = fields.Char(string='Email id')
    address = fields.Char(string='address')
    rented = fields.Many2many('lib.books', string="Rented books")
    image = fields.Binary(string='image')