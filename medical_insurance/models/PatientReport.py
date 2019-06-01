# from odoo import api, models
#
# class PatientReport(models.AbstractModel):
#     _name = 'report.medical_insurance.patient_report_view'
#     @api.model
#     def render_html(self, docids, data=None):
#         report_obj = self.env['report']
#         report = report_obj._get_report_from_name('medical_insurance.patient_report_view')
#         docargs = {
#             'doc_ids': docids,
#             'doc_model': report.model,
#             'docs': self,
#         }
#         return report_obj.render('medical_insurance.patient_report_view', docargs)

