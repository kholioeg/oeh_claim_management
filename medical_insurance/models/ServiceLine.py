from odoo import models, fields, api


class ServiceLine(models.Model):

    _name = 'medical_insurance.service_line'
    #_inherit = "product.product"
    #_inherit = "product.template"
    product = fields.Char()
    sale_price = fields.Float()
    vendor_price = fields.Float()
    patient_price = fields.Float()
    price_plan = fields.Many2one('medical_insurance.price_plan', ondelete='set null', string="PricePlan")
    visit = fields.One2many('medical_insurance.visit', inverse_name='service_line_id', ondelete='set null', string="Visit")





