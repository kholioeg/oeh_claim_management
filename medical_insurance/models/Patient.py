from odoo import models, fields, api,tools


class Patient(models.Model):
    _name = 'medical.insurance.patient'
    _inherit = 'res.partner'

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

    # @api.multi
    # @api.depends('image')
    # def _get_image(self):
    #     for rec in self:
    #         rec.image = tools.image_resize_image_medium(
    #             rec.image, size=(100, 100))