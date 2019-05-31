from odoo import models, fields, api


class DiseaseInfo(models.Model):

    _name = 'medical.insurance.disease_info'
    _inherit = 'res.partner'

