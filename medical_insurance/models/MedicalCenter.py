from odoo import models, fields, api


class MedicalCenter(models.Model):
    _name = 'medical.insurance.medical.center'
    _inherit = 'res.partner'

    price_plan = fields.One2many('medical.insurance.price.plan', inverse_name="medical_center_id", ondelete="set null",
                                 string="PricePlan")
    visit = fields.One2many('medical.insurance.claim', inverse_name="medical_center_id", string="visit")