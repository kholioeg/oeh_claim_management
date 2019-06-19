from dateutil.relativedelta import relativedelta

from dateutil.relativedelta import relativedelta
from odoo import models, fields, api,tools
import datetime

class Patient(models.Model):
    _name = 'medical.insurance.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherits = {'res.partner': 'partner_id'}

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

    price_plan = fields.Many2one('medical.insurance.price.plan', ondelete="set null", string="price plan", required=True)
    plan_cost = fields.Float(string='price plan cost', related='price_plan.plan_cost')
    paid_cost = fields.Float()
    remain_cost = fields.Float(compute='_compute_remain_cost')

    status = fields.Char(compute='_compute_plan_status', string="patient status", readonly=True)
    patient_status = fields.Char(compute='_compute_patient_status', attrs="{'invisible':1}")

    start_date = fields.Date(string="subscription start at", required=True)
    end_date = fields.Date(string="subscription end at", required=True)
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
    @api.onchange('paid_cost')
    def _compute_remain_cost(self):
        self.remain_cost = self.plan_cost - self.paid_cost

    @api.multi
    @api.onchange('status')
    def _compute_patient_status(self):
        self.patient_status = self.status

    @api.multi
    @api.onchange('end_date')
    def _compute_plan_status(self):
        for record in self:
            if record.end_date :
                if fields.Date.today() < record.start_date or fields.Date.today() > record.end_date:
                    self.status = 'Inactive'
                else:
                    self.status = 'Active'

    @api.multi
    @api.onchange('product_id.list_price')
    def onchange_field(self):
        self.plan_cost = self.product_id.list_price


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
