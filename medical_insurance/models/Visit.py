from odoo import models, fields, api


class Visit(models.Model):
    _name = 'medical_insurance.visit'

    patient_id = fields.Many2one('medical_insurance.patient')
    price_plan = fields.Char(related='patient_id.price_plan.name', readonly=True)
    patient_status = fields.Boolean(related='patient_id.status', readonly=True)
    medical_center_id = fields.Many2one('medical_insurance.medical_center')
    service_line_id = fields.Many2one('medical_insurance.service_line')
    contribution_charge = fields.Float(related='service_line_id.vendor_price', readonly=True)
    patient_charge = fields.Float(related='service_line_id.patient_price', readonly=True)

    plan_status = fields.Selection(selection=[
        ('valid', 'Valid'),
        ('not_valid', 'Not Valid')
    ], default=lambda self: self.is_valid(), readonly=True)

    # plan_status = fields.Selection(selection=[
    #     ('valid', 'Valid'),
    #     ('not_valid', 'Not Valid')
    # ], default='valid', readonly=True)

    state = fields.Selection([
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('inprogress', 'Inprogress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='new', readonly=True)

    visit_type = fields.Char(required=True)
    date_of_visit = fields.Datetime(readonly=True, default=lambda self: fields.datetime.now())

    @api.multi
    def is_valid(self):
        if self.patient_status:
            self.plan_status = 'valid'
        else:
            self.plan_status = 'not_valid'

