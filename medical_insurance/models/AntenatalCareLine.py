from odoo import models, fields, api


class AntenatalCareLine(models.Model):
    _name = 'medical.insurance.antenatalcareline'

    patient_id = fields.Many2one('medical.insurance.patient', string='Antenatal Care Line', required=True)

    rx_and_remarks = fields.Char(string="RX & Remarks")
    Wt = fields.Char()
    Date = fields.Date()
    c_o = fields.Char(string="C/O")
    examination_ultrasound = fields.Char(string="Examination Ultrasound")
    BP = fields.Char(string="BP")
