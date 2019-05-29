from odoo import models, fields, api


class Medicine(models.Model):
    _name = 'medical.insurance.medicine'

    patient_id = fields.Many2one('medical.insurance.patient', string='Medicine', required=True)

    medicine = fields.Char()
    indication = fields.Char(string="Indication")
    Start = fields.Date()
    End = fields.Date()
    prescription_reference = fields.Char(string="Prescription Reference")
    dose = fields.Char()
    dose_unit= fields.Char(string="Dose Unit")
    Frequency = fields.Char()
    X = fields.Char()
    treatment_duration = fields.Char(string="Treatment Duration")
    treatment_period = fields.Char(string="Treatment Period")
    Comment = fields.Text()

