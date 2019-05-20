
from odoo import models, fields, api


class EHR(models.Model):
    _name = 'medical.insurance.ehr'

    patient_id = fields.Many2one('medical.insurance.patient', string='Patient EHR', required=True)
    # disease = fields.One2many('medical.insurance.disease',inverse_name="EHR_id",
    #                       ondelete="set null", string="disease", required=True)

    disease = fields.Char()
    severity = fields.Selection([
        ('low', "Low"),
        ('moderate', "Moderate"),
        ('severe', "Severe")
    ])
    status = fields.Selection([
        ('worse', 'Worse'),
        ('improving', 'Improving'),
        ('recovered', 'Recovered')
    ])
    infectious = fields.Boolean()
    diagnosed = fields.Date()
    remarks = fields.Text()

    medicament = fields.Char()
    indication = fields.Char()
    start = fields.Date()
    end = fields.Date()

    vaccine = fields.Char()
    dose = fields.Char()
    Date = fields.Date()
    observation = fields.Selection([
        ('good', 'Good'),
        ('v.good', 'V.good'),
        ('excelent', 'Excellent')
    ])

