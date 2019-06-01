from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'medical.insurance.library.book'
    name = fields.Char()