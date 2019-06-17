from odoo import models, fields, api


class MedicalCenter(models.Model):
    _name = 'medical.insurance.medical.center'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherits = {'res.partner': 'partner_id'}

    price_plan_id = fields.Many2many('medical.insurance.price.plan','rel_price_plan', ondelete="set null", string="PricePlan")
    visit = fields.One2many('medical.insurance.claim', inverse_name="medical_center_id", string="visit")