from odoo import models, fields, api


class Visit(models.Model):
    _name = 'medical.insurance.visit'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('medical.insurance.patient', string='Patient Name', required=True)
    price_plan = fields.Char(string='Price Plane', related='patient_id.price_plan.name', readonly=True)
    patient_status = fields.Boolean(string='Patient Status', related='patient_id.status', readonly=True)
    medical_center_id = fields.Many2one('medical.insurance.medical.center', required=True)
    service_line_id = fields.Many2one('medical.insurance.service.line', string='Service', required=True)
    contribution_charge = fields.Float(string='Contribution Charge', related='service_line_id.vendor_price', readonly=True)
    patient_charge = fields.Float(string='Patient Charge', related='service_line_id.patient_price', readonly=True)
    
    # plan_status = fields.Selection(selection=[
    #     ('valid', 'Valid'),
    #     ('not_valid', 'Not Valid')
    # ], default=lambda self: self.is_valid(), readonly=True)

    plan_status = fields.Selection(selection=[
        ('valid', 'Valid'),
        ('not_valid', 'Not Valid')
    ], default='valid', readonly=True)

    visit_type = fields.Char(required=True)

    visit_state = fields.Selection([
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('inprogress', 'Inprogress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='new', readonly=True)

    #date_of_visit = fields.Datetime(readonly=True, default=lambda self: fields.datetime.now())

    # @api.one
    # @api.depends('id')
    # def comp_name(self):
    #     self.name =  'V '+(self.id)


    # @api.one
    # def is_valid(self):
    #     if self.patient_status:
    #         self.plan_status = 'valid'
    #     else:
    #         self.plan_status = 'not_valid'

