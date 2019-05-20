# from odoo import models, fields, api
#
#
# class Disease(models.Model):
#     _name = 'medical.insurance.disease'
#
#     EHR_id = fields.Many2one('medical.insurance.ehr', string='patient name', required=True)
#     disease = fields.Char()
#     severity = fields.Selection([
#         ('low', "Low"),
#         ('moderate', "Moderate"),
#         ('severe', "Severe")
#     ])
#     status = fields.selection([
#         ('worse', 'Worse'),
#         ('improving', 'Improving'),
#         ('recovered', 'Recovered')
#     ])
#     infectious = fields.Boolean()
#     diagnosed = fields.Date()
#     remarks = fields.Text()
