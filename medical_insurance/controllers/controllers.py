# -*- coding: utf-8 -*-
# from odoo import http


from odoo import http
import json
import logging
from odoo.http import Response, request
_logger = logging.getLogger(__name__)


class MedicalInsurance(http.Controller):

    #patient routes
    @http.route('/api/medical_insurance/patients/', type='http', auth='public', method='GET')
    def medical_patient(self, **kw):
        patients = http.request.env['medical.insurance.patient']
        d = []
        patient = patients.sudo().search([])
        for x in patient:
            d.append({'id': x.id, 'name': x.name})
        return json.dumps({'data': d})


    @http.route('/api/medical_insurance/patient/',type='http', auth='public', method='GET')
    def patient_info_by_id(self, **kwargs):
        Patients = http.request.env['medical.insurance.patient']
        patient_info = []
        patient = Patients.sudo().search([('name', '=', kwargs['mrn'])])
        if patient:
                if patient.patient_status == 'Active':
                    for PricePlan in patient.price_plan:
                        patient_info.append({
                                  'id': patient.id,
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
                        return json.dumps({'data': patient_info})
                else:
                    Response.status = '400'
                    return '{"response": "this patient is Inactive"}'
        else:
            Response.status = '404'
            return '{"response": "not exist"}'



    # create claim / api
    @http.route('/api/medical_insurance/createclaim/', auth='public', methods=['POST'], type='json', csrf=False)
    def apicreateclaim(self, **args):
        data = request.httprequest.data
        res = json.loads(data)
        claim=request.env['medical.insurance.claim'].sudo().create({
            'patient_id' : res['patient_id'],
            'medical_center_id' : res['medical_center_id'],
            'service_line_id' : res['service_line_id'],
            'visit_type' : res['visit_type']
        })

        if claim.claim_status == 'Not Valid':
            return {"response": 404}

        return {'response': 200,
                'name': claim.name,
                'price plan': claim.price_plan,
                'date of visit': claim.date_of_visit,
                'patient status': claim.price_plan_status,
                'contribution charge': claim.contribution_charge,
                'patient charge': claim.patient_charge,
                'claim status' :claim.claim_status,
                'visit type': claim.visit_type,
                'visit state': claim.visit_state,

                }



    #create claim / web

    @http.route('/medical_insurance/claim/new/', type='http', auth="public", methods=['GET'], website=True)
    def get_create_claim_form(self, **kw):
        return http.request.render('medical_insurance.create', {})


    @http.route('/medical_insurance/createclaim/',type='http', auth='public', methods=['POST'], csrf=False)
    def webcreateclaim(self, **kw):
        new_patient = {
            'patient_id': kw['patient_id'],
            'medical_center_id': kw['medical_center_id'],
            'service_line_id': kw['service_line_id'],
            'visit_type': kw['visit_type']
        }
        claim = request.env['medical.insurance.claim'].sudo().create(new_patient)
        print(claim)
        if claim.claim_status == 'Not Valid':
            return http.request.render('medical_insurance.notFound', {})

        return http.request.render('medical_insurance.claim_info', {
            'claims': claim
        })


    # update claim / web

    @http.route('/medical_insurance/claim/update/', type='http', auth="public", methods=['GET'], website=True)
    def get_update_claim_form(self, **kwargs):
        Claims = http.request.env['medical.insurance.claim']
        claims = Claims.sudo().search([('name', '=', kwargs['cl'])])
        return http.request.render('medical_insurance.update', {
            'claims': claims
        })


    @http.route('/medical_insurance/updateclaim/', type='http', auth='public', methods=['POST'], csrf=False)
    def webupdateclaim(self, **kw):
        print(kw)
        id=kw['patient_id']
        update_patient = {
            'patient_id': kw['patient_id'],
            'medical_center_id': kw['medical_center_id'],
            'service_line_id': kw['service_line_id'],
            'visit_type': kw['visit_type']
        }
        cl=request.env['medical.insurance.claim'].sudo().write(update_patient)
        print(cl)






    # @http.route('/medical_insurance/services/', type='http', auth='public', method='GET')
        # def medical_patient(self, **kwargs):
        #     patients = http.request.env['medical.insurance.patient']
        #     d = []
        #     patient = patients.sudo().search(['price_plan', '=', kwargs['price_plan']])
        #     for x in patient:
        #         d.append({'price_plan': x.price_plan})
        #     return json.dumps({'data': d})


    # @http.route('/medical_insurance/updateclaim/', type='http', auth='public', method='POST')
    # def get_claim(self, **kwargs):
    #     data = request.httprequest.data
    #     res = json.loads(data)
    #     request.env['medical.insurance.claim'].sudo().create({
    #         'patient_id': res['patient_id'],
    #         'medical_center_id': res['medical_center_id'],
    #         'service_line_id': res['service_line_id'],
    #         'visit_type': res['visit_type']
    #     })
    #
    #     Claims = http.request.env['medical.insurance.claim']
    #     d = []
    #     claims = Claims.sudo().search([('name', '=', kwargs['cl'])])
    #
    #     for claim in claims:
    #         d.append({
    #                   'name': claim.name,
    #                   'price_plan': claim.price_plan,
    #                   'contribution_charge' : claim.contribution_charge
    #                   })
    #     return json.dumps({'data': d})