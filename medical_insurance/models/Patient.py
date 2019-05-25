from odoo import models, fields, api,tools


class Patient(models.Model):
    _name = 'medical.insurance.patient'
    _inherit = 'res.partner'

    name = fields.Char(string="MRN", readonly=True)
    first_name = fields.Char(string="First name")
    last_name = fields.Char(string="Last name")
    image = fields.Binary()
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
    patient_line = fields.One2many('medical.insurance.patient.line', inverse_name="name", string="patient line", required=True)
    EHR = fields.One2many('medical.insurance.ehr', inverse_name="patient_id", string="EHR", required=True)



    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('medical.insurance.patient') or '/'
        vals['name'] = seq
        return super(Patient, self).create(vals)