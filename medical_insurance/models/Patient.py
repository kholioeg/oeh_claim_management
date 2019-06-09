from dateutil.relativedelta import relativedelta
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


from odoo import models, fields, api,tools


class Patient(models.Model):
    _name = 'medical.insurance.patient'
    _inherit = ['res.partner', 'portal.mixin', 'mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="MRN", readonly=True)
    first_name = fields.Char(string="First name")
    last_name = fields.Char(string="Last name")
    image = fields.Binary()
    NID = fields.Char(string='NID')
    # date_of_birth = fields.Date(string='Birth date')
    birthday = fields.Date(string="DOB")
    age = fields.Integer(string="Age")
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
    # status = fields.Boolean()
    price_plan = fields.Many2one('medical.insurance.price.plan', ondelete="set null", string="price plan")
    patient_status = fields.Char(string='Patient Status', related='price_plan.status', readonly=True, store='True')
    # EHR = fields.One2many('medical.insurance.ehr', inverse_name="patient_id", string="EHR")
    disease = fields.One2many('medical.insurance.disease', inverse_name="patient_id", string="Disease")
    vital_signs_history = fields.One2many('medical.insurance.vitalsignshistory', inverse_name="patient_id", string="Vital Signs")
    operation_reservation = fields.One2many('medical.insurance.operationreservation', inverse_name="patient_id", string="Operation Reservation")
    medicine = fields.One2many('medical.insurance.medicine', inverse_name="patient_id", string="Medicine")
    antenatal_care = fields.One2many('medical.insurance.antenatalcareline', inverse_name="patient_id", string="Antenatal Care Line")

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('medical.insurance.patient') or '/'
        vals['name'] = seq

        return super(Patient, self).create(vals)


    @api.multi
    @api.onchange('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday and record.birthday <= fields.Date.today():
                record.age = relativedelta(
                    fields.Date.from_string(fields.Date.today()),
                    fields.Date.from_string(record.birthday)).years
            else:
                record.age = 0


    @api.multi
    def name_get(self, context=None):
        if context is None:
            context = {}
        result = []
        for record in self:
            if self.env.context.get('custom_search', True):
                name = '[{}] {} - {}'.format (record.name, record.first_name, record.last_name)
                # name = '[' + str(record.name) + ']' + ' ' + record.first_name

                result.append((record.id, name))

        return result

