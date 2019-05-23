from odoo import models, fields, api


class Visit(models.Model):
    _name = 'medical.insurance.claim'

    name = fields.Char(string="Claim No", readonly=True, required=True, copy=False, default='New', store='True')
    # patient_id = fields.Many2one('medical.insurance.patient.line', string='Patient Name', required=True, store='True')
    # price_plan = fields.Char(string='Price Plane', related='patient_id.price_plan.name', readonly=True, store=True)
    # price_plan_status = fields.Char(string='Patient Status', related='patient_id.plan_status', readonly=True, store='True')
    medical_center_id = fields.Many2one('medical.insurance.medical.center', required=True, store='True')
    service_line_id = fields.Many2one('medical.insurance.service.line', string='Service', required=True, store='True')
    contribution_charge = fields.Float(string='Contribution Charge', related='service_line_id.vendor_price', readonly=True, store='True')
    patient_charge = fields.Float(string='Patient Charge', related='service_line_id.patient_price', readonly=True, store='True')
    date_of_visit = fields.Datetime(default=lambda self: fields.datetime.now(), store='True')
    # claim_status = fields.Char(compute='compute_claim_status', readonly=True)
    visit_type = fields.Selection([
        ('office', 'Office Visit'),
        ('physical', 'Physical'),
        ('school', 'School/Sports Physical'),
        ('exam', 'Medicare Initial Preventative Physical Exam'),
        ('labs', 'Screening and Diagnostic labs'),
    ], required=True, store='True')
    visit_state = fields.Selection([
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('progress', 'In progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='new', readonly=True, store='True')


    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('medical.insurance.claim') or '/'
        vals['name'] = seq
        return super(Visit, self).create(vals)

    # @api.one
    # def compute_claim_status(self):
    #     if self.price_plan_status == 'Active' and self.patient_id.price_plan.medical_center_id and self.patient_id.price_plan.service_line:
    #         for med in self.patient_id.price_plan.medical_center_id:
    #             if med.name == self.medical_center_id.name:
    #                 for s in self.patient_id.price_plan.service_line:
    #                     if s.name == self.service_line_id.name:
    #                         self.claim_status = 'Valid'
    #                         break
    #                     else:
    #                         self.claim_status = 'Not Valid'
    #                 break
    #             else:
    #                 self.claim_status = 'Not Valid'
    #     else:
    #         self.claim_status = 'Not Valid'
