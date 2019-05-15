from odoo import models, fields, api


class Patient(models.Model):
    _name = 'medical_insurance.patient'
    _inherit = 'res.partner'
    name = fields.Char(string='Name')
    NID = fields.Char(string='NID')
    date_of_birth = fields.Date(string='Birth date')
    gender = fields.Selection([
        ('male', "Male"),
        ('female', "Female"),
    ])

    mariage_state = fields.Selection([
        ('single', "Single"),
        ('maried', "Maried"),
    ], default="single")
    blood_group = fields.Char(string='blood group')
    weight = fields.Float()
    height = fields.Float()
    status = fields.Boolean()
    visit = fields.One2many('medical_insurance.visit', inverse_name="patient_id",ondelete="set null", string="visit")
    price_plan = fields.Many2one('medical_insurance.price_plan', ondelete="set null", string="Price plan")
