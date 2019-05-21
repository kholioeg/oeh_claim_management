from odoo import models, fields, api


class ServiceLine(models.Model):

    _name = 'medical.insurance.service.line'
    name = fields.Many2one('product.template', string="Product")
    sale_price = fields.Float(related="name.list_price")
    vendor_price = fields.Float()
    patient_price = fields.Float()
    price_plan = fields.Many2one('medical.insurance.price.plan', string="Price Plan")
    # visit = fields.One2many('medical.insurance.claim', inverse_name='service_line_id',
    #                         string="Visit")
    #


@api.onchange('name.list_price')
def onchange_field(self):
    self.sale_price = self.name.list_price
