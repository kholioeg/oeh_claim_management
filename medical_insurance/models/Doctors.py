from odoo import models, fields, api


class Doctors(models.Model):

    _name = 'medical.insurance.doctors'
    _inherit = 'res.partner'

