from odoo import models, fields, api


class Patient(models.Model):
    _name = 'medical_insurance.patient'
    _inherit = 'res.partner'
    first_name = fields.Char()
    last_name = fields.Char()
    NID = fields.Integer()
    date_of_birth = fields.Date()
    gender = fields.Selection([
        ('male', "Male"),
        ('female', "Female"),
    ])

    mariage_state = fields.Selection([
        ('single', "Single"),
        ('maried', "Maried"),
    ], default="single")
    blood_group = fields.Char()
    weight = fields.Float()
    height = fields.Float()
    status = fields.Boolean()
    visit = fields.One2many('medical_insurance.visit', inverse_name="patient_id",ondelete="set null", string="visit")
    price_plan = fields.Many2one('medical_insurance.price_plan', ondelete="set null", string="PricePlan")
