from odoo import models, fields, api,tools


class Patient(models.Model):
    _name = 'medical.insurance.patient'
    _inherit = 'res.partner'

    name = fields.Char(string="patient no", readonly=True)
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
    price_plan = fields.Many2one('medical.insurance.price.plan', ondelete="set null", string="price plan",
                                 required=True)
    EHR = fields.One2many('medical.insurance.ehr', inverse_name="patient_id", string="EHR", required=True)

    # @api.multi
    # @api.depends('image')
    # def _get_image(self):
    #     for rec in self:
    #         rec.image = tools.image_resize_image_medium(
    #             rec.image, size=(100, 100))

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('medical.insurance.patient') or '/'
        vals['name'] = seq
        return super(Patient, self).create(vals)