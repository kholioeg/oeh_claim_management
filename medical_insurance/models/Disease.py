from odoo import models, fields, api


class Disease(models.Model):
    _name = 'medical.insurance.disease'

    patient_id = fields.Many2one('medical.insurance.patient', string='Disease', required=True)

    disease = fields.Char()
    severity = fields.Selection([
        ('low', "Low"),
        ('moderate', "Moderate"),
        ('severe', "Severe")
    ])
    state = fields.Selection([
        ('worse', 'Worse'),
        ('improving', 'Improving'),
        ('recovered', 'Recovered')
    ])
    infectious = fields.Boolean()
    diagnosed_on = fields.Date()
    remarks = fields.Text()
