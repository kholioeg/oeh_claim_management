from odoo import models, fields, api


class MedicalCenter(models.Model):
    _name = 'medical.insurance.medical.center'
    _inherits = {'res.partner': 'partner_id'}

    price_plan_id = fields.Many2many('medical.insurance.price.plan','rel_price_plan', ondelete="set null", string="PricePlan")
    visit = fields.One2many('medical.insurance.claim', inverse_name="medical_center_id", string="visit")


    @api.multi
    @api.onchange('name')
    def onchange_field(self):
        print("on change2")
        res = self.env['res.partner'].create({'name': self.name})
        self.partner_id = res.id

    # @api.multi
    # @api.model
    # def total_invoice(self):
    #     if self.visit:
    #         for v in self.visit.invoice_id:
    #             print('medinvoice')
    #             print(v.number)
