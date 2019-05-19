
from odoo import models, fields, api


class EHR(models.Model):
    _name = 'medical.insurance.ehr'


    patient_id = fields.Many2one('medical.insurance.patient', string='Patient EHR', required=True)