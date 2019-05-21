from odoo import models, fields, api
import datetime
class PatientLine(models.Model):

    _name = 'medical.insurance.patient.line'

    price_plan = fields.Many2one('medical.insurance.price.plan',
                                 string="PricePlan")
    name = fields.Many2one('medical.insurance.patient', ondelete="set null",
                                 string="Patient")
    paid_cost = fields.Float()
    remain_cost = fields.Float(compute='_compute_remain_cost')
    plan_status = fields.Char(compute='_compute_plan_status', readonly=True)
    status = fields.Boolean()

    visit = fields.One2many('medical.insurance.visit', inverse_name="patient_id", ondelete="set null", string="visit",
                            required=True)

    @api.one
    def _compute_remain_cost(self):
        self.remain_cost = self.price_plan.price - self.paid_cost

    @api.one
    def _compute_plan_status(self):
        for rec in self.price_plan:
            today = datetime.datetime.now().date()
            start = self.price_plan.start_date
            end = self.price_plan.end_date
            if today <= start or today >= end:
                self.plan_status = 'Inactive'
            else :
                self.plan_status = 'Active'




