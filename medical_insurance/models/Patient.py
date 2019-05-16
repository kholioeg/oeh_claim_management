from odoo import models, fields, api


class Patient(models.Model):
    _name = 'medical_insurance.patient'
    _inherit = 'res.partner'

    name = fields.Char(
        track_visibility='onchange'
    )
    email = fields.Char(
        track_visibility='onchange'
    )
    phone = fields.Char(
        track_visibility='onchange'
    )
    NID = fields.Char(string='NID')
    date_of_birth = fields.Date(string='Birth date')
 
    gender = fields.Selection([
        ('male', "Male"),
        ('female', "Female"),
    ])

    marital_status = fields.Selection([
        ('single', "Single"),
        ('married', "Married"),
    ], default="single")
    blood_group = fields.Char(string='blood group')
    weight = fields.Float()
    height = fields.Float()
    status = fields.Boolean()
    visit = fields.One2many('medical_insurance.visit', inverse_name="patient_id", ondelete="set null", string="visit", required=True)
    price_plan = fields.Many2one('medical_insurance.price_plan', ondelete="set null", string="Price plan")
