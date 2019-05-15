from odoo import models, fields, api

class MedicalCenter(models.Model):
    _name = 'medical_insurance.medical_center'
    _inherit = 'res.partner'

    price_plan = fields.One2many('medical_insurance.price_plan', inverse_name="medical_center_id", ondelete="set null", string="PricePlan")
    visit = fields.One2many('medical_insurance.visit', inverse_name="medical_center_id", ondelete="set null", string="visit")