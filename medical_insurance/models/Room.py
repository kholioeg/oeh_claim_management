from odoo import models, fields, api


class Room(models.Model):

    _name = 'medical.insurance.room'
    _inherit = 'res.partner'

