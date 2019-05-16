from odoo import models, fields, api


class Visit(models.Model):
    _name = 'medical_insurance.visit'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('medical_insurance.patient', string='Patient Name', required=True)
    price_plan = fields.Char(string='Price Plane', related='patient_id.price_plan.name', readonly=True)
    patient_status = fields.Boolean(string='Patient Status', related='patient_id.status', readonly=True)
    medical_center_id = fields.Many2one('medical_insurance.medical_center', required=True)
    service_line_id = fields.Many2one('medical_insurance.service_line', string='Service', required=True)
    contribution_charge = fields.Float(string='Contribution Charge', related='service_line_id.vendor_price', readonly=True)
    patient_charge = fields.Float(string='Patient Charge', related='service_line_id.patient_price', readonly=True)
    date_of_visit = fields.Datetime(readonly=True, default=lambda self: fields.datetime.now())
    visit_type = fields.Char(required=True)
    plan_status = fields.Char(compute='compute_plan_status', readonly=True)

    visit_state = fields.Selection([
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('inprogress', 'Inprogress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='new', readonly=True)


    @api.one
    def compute_plan_status(self):
        if self.patient_status:
            self.plan_status = 'valid'
            for p in self.patient_id.price_plan.patient:
                if p.name==self.patient_id.name:
                    for med in self.medical_center_id.price_plan.medical_center_id:
                        if med.name == self.medical_center_id.name:
                            for s in self.service_line_id.price_plan.service_line:
                                if s.name == self.service_line_id.name:
                                    self.plan_status = 'valid'
                                else:
                                    self.plan_status = 'not_valid'
                        else:
                            self.plan_status = 'not_valid'
                else:
                    self.plan_status = 'not_valid'
        else:
            self.plan_status = 'not_valid'
