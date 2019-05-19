from odoo import models, fields, api

class PatientLine(models.Model):
    _name = 'medical.insurance.patient.line'

    price_plan = fields.Many2one('medical.insurance.price.plan',
                                 string="PricePlan")
    patient = fields.Many2one('medical.insurance.patient', ondelete="set null",
                                 string="Patient")
    paid_cost = fields.Float()
    remain_cost = fields.Float(compute='_compute_remain_cost')
    # patient_status = fields.Boolean(string='Patient Status', related='patient_id.status', readonly=True)

    @api.one
    def _compute_remain_cost(self):
        self.remain_cost =  self.price_plan.price - self.paid_cost

