from odoo import models, fields, api

class Visit(models.Model):

    _name = 'medical.insurance.visit'
    name = fields.Char(string="Claim No", readonly=True, required=True, copy=False, default='New')
    patient_id = fields.Many2one('medical.insurance.patient', string='Patient Name', required=True)
    price_plan = fields.Many2one(string='Price Plane', readonly=True)
    patient_status = fields.Boolean(string='Patient Status', related='patient_id.status', readonly=True)
    medical_center_id = fields.Many2one('medical.insurance.medical.center', required=True)
    service_line_id = fields.Many2one('medical.insurance.service.line', string='Service', required=True)
    contribution_charge = fields.Float(string='Contribution Charge', related='service_line_id.vendor_price', readonly=True)
    patient_charge = fields.Float(string='Patient Charge', related='service_line_id.patient_price', readonly=True)
    date_of_visit = fields.Datetime(default=lambda self: fields.datetime.now())
    plan_status = fields.Char(compute='compute_plan_status', readonly=True)
    visit_type = fields.Selection([
        ('office', 'Office Visit'),
        ('physical', 'Physical'),
        ('school', 'School/Sports Physical'),
        ('exam', 'Medicare Initial Preventative Physical Exam'),
        ('labs', 'Screening and Diagnostic labs'),
    ], required=True)
    visit_state = fields.Selection([
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('progress', 'In progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='new', readonly=True)


    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('medical.insurance.visit') or '/'
        vals['name'] = seq
        return super(Visit, self).create(vals)

    @api.one
    def compute_plan_status(self):
        if self.patient_status:
            print(self.patient_id)
            for p in self.patient_id.price_plan.patient:
                if p.name==self.patient_id.name:
                    for med in self.medical_center_id.price_plan.medical_center_id:
                        if med.name == self.medical_center_id.name:
                            for s in self.service_line_id.price_plan.service_line:
                                if s.name == self.service_line_id.name:
                                    self.plan_status = 'Valid'
                                    break
                                else:
                                    self.plan_status = 'Not Valid'
                            break
                        else:
                            self.plan_status = 'Not Valid'
                    break
                else:
                    self.plan_status = 'Not Valid'
        else:
            self.plan_status = 'Not Valid'
