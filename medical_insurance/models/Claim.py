from odoo import models, fields, api

class Visit(models.Model):
    _name = 'medical.insurance.claim'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Claim No", readonly=True, required=True, copy=False, default='New', store='True')
    patient_id = fields.Many2one('medical.insurance.patient', string='Patient Name', required=True, store='True',
                                 ondelete='set null')
    price_plan = fields.Char(string='Price Plane', related='patient_id.price_plan.name', readonly=True, store=True)
    price_plan_status = fields.Char(string='Patient Status', related='patient_id.status', readonly=True,
                                    store='True')
    medical_center_id = fields.Many2one('medical.insurance.medical.center', required=True, store='True',
                                        ondelete='set null')
    service_line_id = fields.Many2one('medical.insurance.service.line', string='Service', required=True, store='True',
                                      ondelete='set null')
    contribution_charge = fields.Float(string='Contribution Charge', related='service_line_id.vendor_price',
                                       readonly=True, store='True')
    patient_charge = fields.Float(string='Patient Charge', related='service_line_id.patient_price', readonly=True,
                                  store='True')
    date_of_visit = fields.Datetime(default=lambda self: fields.datetime.now(), store='True')
    claim_status = fields.Char(compute='compute_claim_status', readonly=True, store='True')
    visit_type = fields.Selection([
        ('outpatient', 'Outpatient'),
        ('ambulatory', 'Ambulatory'),
        ('opd/er', 'OPD/ER'),
    ], required=True)
    visit_state = fields.Selection([
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('progress', 'In progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='new')
    service_line_type = fields.Char(string="Service Type", related='service_line_id.service_type', readonly=True)
    invoice_id = fields.Many2one('account.invoice', string="Invoice")

    # Blood_Group = fields.Char()
    history = fields.Text(string="History And Clinical Examination:")
    care_plan = fields.Text(string="Plan Of Care:")
    diagnosis = fields.Text(string="DIAGNOSIS:")
    instructions = fields.Text(string="INSTRUCTIONS:")
    temperature = fields.Boolean(string="Temperature")
    pulse_rate = fields.Boolean(string="Pulse Rate")
    respiratory_rate = fields.Boolean(string="Respiratory Rate")
    blood_pressure = fields.Boolean(string="Blood Pressure")
    o2_saturation = fields.Boolean(string="O2 Saturation")
    pain_score = fields.Boolean(string="Pain Score")

    clinical_comments = fields.Text(string="clinical comments:")
    Requested_by = fields.Text(string="Requested by")
    stamp_and_signature = fields.Text(string="Stamp & signature")
    lab_date = fields.Date(string="Date")
    requested_test = fields.Text(string="Requested test:")
    results = fields.Text(string="Results:")
    Pathologist = fields.Char(string="Pathologist:")
    Examiner_Name = fields.Char(string="Examiner Name:")
    routine = fields.Boolean('routine')
    Urgent = fields.Boolean('Urgent')
    pre_operative = fields.Boolean('pre_operative')
    # routine = fields.Boolean('routine')

    referring_physician = fields.Char()
    resident = fields.Boolean('Resident')
    specialist = fields.Boolean('Specialist')
    consultant = fields.Boolean('Consultant')
    # degree_of_urgency = fields.Char()
    routine = fields.Boolean('Routine')
    semi_urgent = fields.Boolean('Semi urgent')
    urgent = fields.Boolean('Urgent')
    life_saving = fields.Boolean('Life saving')

    peripheral_line = fields.Boolean('Peripheral line')
    cutdown = fields.Boolean('Cutdown')
    port_a_cath = fields.Boolean('Port A cath')
    central_line = fields.Boolean('Central line')

    days = fields.Boolean('Days')
    more_than_2_weeks = fields.Boolean('More than 2 weeks')

    blood_exchange = fields.Boolean('Blood exchange ')
    tpn = fields.Boolean('TPN')
    chemotherapy = fields.Boolean('Chemotherapy')
    coagulopathy = fields.Boolean('Coagulopathy')

    yes = fields.Boolean('Yes')
    no = fields.Boolean('No')

    removal_reason = fields.Text(string="for removal reason :")
    surgical_note = fields.Text(string="Surgical note :")
    anesthetist_note = fields.Text(string="Anesthetist note :")
    procedure = fields.Text(string="Procedure :")

    physician_name = fields.Text(string="Physician Name :")
    stamp_signature = fields.Text(string="Stamp & Signature :")
    date = fields.Date(string="Date")

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('medical.insurance.claim') or '/'
        vals['name'] = seq
        return super(Visit, self).create(vals)

    @api.multi
    def write(self, vals):
        result = super(Visit, self).write(vals)
        if self.visit_state == 'confirmed':
            if self.claim_status == 'Valid' and not self.invoice_id:
                res_id = self.env['account.invoice'].create({
                    'partner_id': self.medical_center_id.partner_id.id,
                })
                self.env['account.invoice.line'].create({
                    'invoice_id': res_id.id,
                    'product_id': self.service_line_id.name.id,
                    'account_id': self.service_line_id.name.id,
                    'quantity': 1.00,
                    'name': self.service_line_id.name.name,
                    'price_unit': self.contribution_charge,
                })
                res_id.action_invoice_open()
                self.write({'invoice_id': res_id.id})
        return result

    @api.one
    @api.depends('patient_id', 'patient_id.price_plan.medical_center_id', 'patient_id.price_plan.service_line',
                 'price_plan_status')
    def compute_claim_status(self):
        print(self.id)
        if self.price_plan_status == 'Active' and self.patient_id.price_plan.medical_center_id and self.patient_id.price_plan.service_line:
            for med in self.patient_id.price_plan.medical_center_id:
                if med.name == self.medical_center_id.name:
                    for s in self.patient_id.price_plan.service_line:
                        if s.name == self.service_line_id.name:
                            self.claim_status = 'Valid'
                            break
                        else:
                            self.claim_status = 'Not Valid'
                    break
                else:
                    self.claim_status = 'Not Valid'
        else:
            self.claim_status = 'Not Valid'

    @api.one
    @api.depends('visit_state')
    def post_a_message(self):
        self.message_post(body='nada')