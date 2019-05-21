from odoo import models, fields, api


class Patient(models.Model):
    _name = 'medical.insurance.patient'
    _inherit = 'res.partner'
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

    EHR = fields.One2many('medical.insurance.ehr', inverse_name="patient_id", string="EHR", required=True)
