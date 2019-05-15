from odoo import models, fields, api

class PricePlan(models.Model):
    _name = 'medical_insurance.price_plan'
    name = fields.Char(string="Name",required=True)
    start_date = fields.Date(string="Start At",required=True)
    end_date = fields.Date(string="End At",required=True)
    state = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], default='active')
    #patient = fields.One2many('medical_insurance.Patient',inverse_name='patient',ondelete='set null'. string='Patient', required='True')
    #medical_center = fields.Many2one('medical_insurance.MedicalCentre', ondelete='set null',string='MedicalCentre', required='True')
    #service_line= fields.One2many('medical_insurance.ServiceLine',inverse_name='service_line',ondelete='set null', string='ServiceLine', required='True')


