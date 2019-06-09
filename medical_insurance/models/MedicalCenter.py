from odoo import models, fields, api


class MedicalCenter(models.Model):
    _name = 'medical.insurance.medical.center'
    _inherit = ['res.partner', 'account.invoice']

    price_plan_id = fields.Many2many('medical.insurance.price.plan','rel_price_plan', ondelete="set null", string="PricePlan")
    visit = fields.One2many('medical.insurance.claim', inverse_name="medical_center_id", string="visit")
    medical_center_invoice = fields.Many2one('account.invoice', string="Invoice")