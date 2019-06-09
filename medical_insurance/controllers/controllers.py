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
from reportlab.lib import yaml

from odoo import http
import json
import logging

from odoo.addons.payment_ogone import data
from odoo.exceptions import ValidationError
from odoo.http import Response, request

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



    @http.route('/medical_insurance/patient/',type='http', auth='public', method='GET')
    def patient_info_by_id(self, **kwargs):
        Patients = http.request.env['medical.insurance.patient']
        d = []
        patients = Patients.sudo().search([('name', '=', kwargs['mrn'])])

        if patients.exists():
            for patient in patients:
                if patient.patient_status == 'Active':
                    # print (patient.patient_status)
                    for PricePlan in patients.price_plan:
                        d.append({'id': patient.id,
                                  'MRN': patient.name,
                                  'first_name' : patient.first_name,
                                  'last_name' : patient.last_name,
                                  'patient_status' : patient.patient_status,
                                  'NID' : patient.NID,
                                  'age' : patient.age,
                                  'gender' : patient.gender,
                                  'marital_status' : patient.marital_status,
                                  'price_plan' : PricePlan.name
                                  })
                        return json.dumps({'data': d})
                else:
                    Response.status = '400'
                    return '{"response": "this patient is Inactive"}'
        else:
            Response.status = '404'
            return '{"response": "not exist"}'



    # @http.route('/medical_insurance/createclaim', methods=['POST'], type='http', csrf=False, auth="public")
    # def createClaim(self, **kwargs):
    #     return Response(json.dumps({"yes": "asmaaaaa"}), content_type='application/json;charset=utf-8', status=200)



    #static name
    # @http.route('/medical_insurance/createbook/', auth='public', methods=['POST'], type='http',csrf=False)
    # def index(self, **args):
    #     name = args.get('name', False)
        # if not name:
        #     Response.status = '400 Bad Request'
        # return '{"response": "OK"}'
        # request.env['medical.insurance.library.book'].sudo().create({
        #         'name' :args.get('name', "java book")
        #     })

    # @http.route('/medical_insurance/createbook', methods=['POST'], type='http', csrf=False, auth="public")
    # def _process_registration(self, post):
    #     request.env['medical.insurance.library.book'].sudo().create({
    #         'name' : "python book"
    #     })
    # return Response(json.dumps({"yes": "book created"}), content_type='application/json;charset=utf-8', status=200)
    #

    #test working
    @http.route('/medical_insurance/createbook/', auth='public', methods=['POST'], type='json', csrf=False)
    def index(self, **params):
        data = request.httprequest.data
        res = json.loads(data)
        print (res['name'])
        request.env['medical.insurance.library.book'].sudo().create({
        'name': res['name']
        })

    @http.route('/medical_insurance/createclaim/', auth='public', methods=['POST'], type='json', csrf=False)
    def index(self, **params):
        data = request.httprequest.data
        res = json.loads(data)

        request.env['medical.insurance.claim'].sudo().create({

            'patient_id' : res['patient_id'],
            'medical_center_id' : res['medical_center_id'],
            'service_line_id' : res['service_line_id'],
            'visit_type' : res['visit_type']
            # 'contribution_charge' : res['contribution_charge']
        })




        # if not patients.exists():
        #         Response.status = '404'
        #         return '{"response": "not exist"}'