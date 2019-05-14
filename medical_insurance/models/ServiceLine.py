from odoo import models, fields, api


class ServiceLine(models.Model):

    _name = 'medical_insurance.service_line'
    product = fields.Char()
    sale_price = fields.Integer()
    vendor_price = fields.Integer()
    patient_price = fields.Integer()
    #price_plane = fields.Many2one('medical_insurance.PricePlan', ondelete='set null', string="PricePlan")
    #visit = fields.One2many('medical_insurance.Visit', inverse_name='visit', ondelete='set null', string="Visit")





