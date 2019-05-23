from odoo import models, fields, api


class PricePlan(models.Model):
    _name = 'medical.insurance.price.plan'
    _inherit = 'product.template'

    name = fields.Char(string="Name", required=True)
    price = fields.Float()
    state = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], default='active')
    start_date = fields.Date(string="Start At", required=True)
    end_date = fields.Date(string="End At", required=True)
    medical_center_id = fields.Many2one('medical.insurance.medical.center', ondelete='set null', string='MedicalCenter',
                                        required='True')
    patient = fields.One2many('medical.insurance.patient', inverse_name='price_plan', ondelete='set null',
                                   string='Patient', required='True')

    service_line = fields.One2many('medical.insurance.service.line', inverse_name='price_plan', ondelete='set null',
                                   string='ServiceLine', required='True')


