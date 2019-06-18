from odoo import models, fields, api

class VitalSignsHistory(models.Model):
    _name = 'medical.insurance.vitalsignshistory'

    patient_id = fields.Many2one('medical.insurance.patient', string='Patient MRN', required=True)

    VB = fields.Char(string="VB")
    F1_O2 = fields.Char(string="F1 O2")
    RR_SPO2 = fields.Char(string="R.R/SPO2")
    remarks = fields.Text(string="Remarks")
    sao2 = fields.Char(string="Sa O2")
    # patient_num = fields.One2many('medical.insurance.patient',string="patient id")
    T= fields.Char(string="T.")
    BP = fields.Char(string="BP")
    HR = fields.Char(string="HR")
    date_time = fields.Datetime()
    D = fields.Char(string="D")
    P =fields.Char(string="P.")
    FHS = fields.Char(string="FHS")
