# -*- coding: utf-8 -*-
# from odoo import http

# class MedicalInsurance(http.Controller):
#     @http.route('/medical_insurance/medical_insurance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/medical_insurance/medical_insurance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('medical_insurance.listing', {
#             'root': '/medical_insurance/medical_insurance',
#             'objects': http.request.env['medical_insurance.medical_insurance'].search([]),
#         })

#     @http.route('/medical_insurance/medical_insurance/objects/<model("medical_insurance.medical_insurance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('medical_insurance.object', {
#             'object': obj
#         })


# from odoo import http
# from odoo.http import request
#
#
# class PatientData(http.Controller):
#
#     @http.route('/patient_validate/', type='http', auth='none', methods=['GET'])
#     def patient_details(self, **kwargs):
#         #pa_details = request.env['medical.insurance.patient'].sudo().search([])
#         #if(pa_details):
#         return request.render('', None)

from odoo import http
import json
import logging

_logger = logging.getLogger(__name__)




class MedicalInsurance(http.Controller):
    @http.route('/medical_insurance/patient_validate/', auth='public')
    def index(self, **kw):
        return json.dumps({'result': 'Test result'})


#working asmaa
# from odoo import http, registry
#
# class Main(http.Controller):
#
#
#     @http.route('/medical_insurance/book/', type='http', auth='public')
#     def books_json(self , **kw):
#         return http.request.render('medical_insurance.index', {
#             'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
#         })

# class Main(http.Controller):
#
#     @http.route('/medical_insurance/book/', type='http', auth='public')
#     def books_json(self , **kw):
#         Teachers = http.request.env['medical.insurance.library.book']
#         return http.request.render('medical_insurance.index', {
#             'teachers': Teachers.search([])
#         })

#test book
 # @http.route('/medical_insurance/book/', type='http', auth='public')
 #    def books_json(self, **kw):
 #        Teachers = http.request.env['medical.insurance.library.book']
 #        return http.request.render('medical_insurance.index', {
 #            'teachers': Teachers.search([])
 #        })


class MedicalCenter(http.Controller):

    @http.route('/medical_insurance/center/',type='http', auth='public' , method='GET')
    def medical_center(self , **kw):
        Centers = http.request.env['medical.insurance.medical.center']
        d = []
        center = Centers.sudo().search([])
        for x in center:
            d.append({'id': x.id, 'name': x.name})
        return json.dumps({'data': d})
        # })

    # @http.route('/medical_insurance/patient_validate/', type='http', auth='public')
    # def patient_info(self, **kw):
    #     Patients = http.request.env['medical.insurance.patient']
    #     return http.request.render('medical_insurance.index', {
    #         'patients': Patients.search([])
    #     })
    @http.route('/medical_insurance/patients/', type='http', auth='public', method='GET')
    def medical_patient(self, **kw):
        patients = http.request.env['medical.insurance.patient']
        d = []
        patient = patients.sudo().search([])
        for x in patient:
            d.append({'id': x.id, 'name': x.name})
        return json.dumps({'data': d})

    @http.route('/medical_insurance/patient/<int:id>/',type='http', auth='public', method='GET')
    def patient_info_by_id(self, id):
        Patients = http.request.env['medical.insurance.patient']
        d = []
        patient = Patients.sudo().search([])
        for patients in patient[id]:
            for PricePlan in patients.price_plan:
                d.append({'id': patients.id,
                          'MRN': patients.name,
                          'first_name' : patients.first_name,
                          'last_name' : patients.last_name,
                          'patient_status' : patients.patient_status,
                          'NID' : patients.NID,
                          'age' : patients.age,
                          'gender' : patients.gender,
                          'marital_status' : patients.marital_status,
                          'price_plan' : PricePlan.name,
                          })
        return json.dumps({'data': d})









