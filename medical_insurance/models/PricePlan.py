from odoo import models, fields, api
import datetime


class PricePlan(models.Model):
    _name = 'medical.insurance.price.plan'
    _inherits = {'product.template':'product_id'}

    product_id = fields.Many2one('product.template', ondelete='cascade')
    name = fields.Char(related="product_id.name")
    plan_cost = fields.Float(related="product_id.list_price")
    paid_cost = fields.Float()
    remain_cost = fields.Float(compute='_compute_remain_cost')
    status = fields.Char(compute='_compute_plan_status', readonly=True)
    start_date = fields.Date(string="Start At")
    end_date = fields.Date(string="End At")
    # price = fields.Float()
    medical_center_id = fields.Many2one('medical.insurance.medical.center', ondelete='set null', string='MedicalCenter')
    patient = fields.One2many('medical.insurance.patient', inverse_name='price_plan', ondelete='set null',
                              string='Patient')
    service_line = fields.One2many('medical.insurance.service.line', inverse_name='price_plan', ondelete='set null',
                                   string='ServiceLine')
    @api.one
    def _compute_plan_status(self):
        for rec in self :
            today = datetime.datetime.now().date()
            start = self.start_date
            end = self.end_date
            if today <= start or today >= end:
                self.status = 'Inactive'
            else:
                self.status = 'Active'

    @api.one
    def _compute_remain_cost(self):
        self.remain_cost = self.plan_cost - self.paid_cost

    @api.onchange('product_id.list_price')
    def onchange_field(self):
        self.plan_price = self.product_id.list_price