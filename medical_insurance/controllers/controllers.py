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

class Main(http.Controller):

    @http.route('/medical_insurance/book/', type='http', auth='public')
    def books_json(self , **kw):
        Teachers = http.request.env['medical.insurance.library.book']
        return http.request.render('medical_insurance.index', {
            'teachers': Teachers.search([])
        })


class MedicalCenter(http.Controller):

    @http.route('/medical_insurance/center/',type='http', auth='public')
    def medical_center(self , **kw):
        Centers = http.request.env['medical.insurance.medical.center']
        return http.request.render('medical_insurance.centers',{
            'centers':Centers.search([])
        })



