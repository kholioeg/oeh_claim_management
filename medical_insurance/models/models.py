# -*- coding: utf-8 -*-

from odoo import models, fields, api

<<<<<<< HEAD

class medical_insurance(models.Model):
     _name = 'medical_insurance.medical_insurance'

=======
class medical_insurance(models.Model):
    _name = 'medical_insurance.medical_insurance'
>>>>>>> 3b3401e5d2fe0b57b1d3b00ff0d10a9e4907261a

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100