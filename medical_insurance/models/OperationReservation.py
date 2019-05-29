from odoo import models, fields, api


class OperationReservation(models.Model):

    _name = 'medical.insurance.operationreservation'
    _inherit = 'res.partner'

    name = fields.Char(string="Operation No", readonly=True,store='True')
    patient_id = fields.Many2one('medical.insurance.patient', string='patient', required=True)
    From = fields.Datetime()
    To = fields.Datetime()
    Notes = fields.Text()
    doctor_name = fields.Many2one('medical.insurance.doctors', string="doctor")
    # doctor_id = fields.Char(related="doctor_name ")

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('medical.insurance.operationreservation') or '/'
        vals['name'] = seq
        return super(OperationReservation, self).create(vals)