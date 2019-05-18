from odoo import models, fields, api


class ServiceLine(models.Model):

    _name = 'medical.insurance.service.line'
    name = fields.Many2one('product.template', string="Product")
    sale_price = fields.Float()
    vendor_price = fields.Float()
    patient_price = fields.Float()
    price_plan = fields.Many2one('medical.insurance.price.plan', ondelete='set null', string="Price Plan")
    visit = fields.One2many('medical.insurance.visit', inverse_name='service_line_id', ondelete='set null',
                            string="Visit")





