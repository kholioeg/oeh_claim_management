from odoo import models, fields, api


class DiseaseInfo(models.Model):

    _name = 'medical.insurance.disease_info'
    name = fields.Char(string="Disease Name")

