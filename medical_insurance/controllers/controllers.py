# -*- coding: utf-8 -*-
# from odoo import http
import args as args

from odoo import http
import json
import logging
from odoo.http import Response, request
_logger = logging.getLogger(__name__)


class MedicalInsurance(http.Controller):


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




    @http.route('/medical_insurance/services/', type='http', auth='public', method='GET')
    def medical_patient(self, **kwargs):
        patients = http.request.env['medical.insurance.patient']
        d = []
        patient = patients.sudo().search(['price_plan', '=', kwargs['price_plan']])
        for x in patient:
            d.append({'price_plan': x.price_plan})
        return json.dumps({'data': d})




    @http.route('/medical_insurance/createclaim/', auth='public', methods=['POST'], type='json', csrf=False)
    def index(self, **args):
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




    
    @http.route('/medical_insurance/updateclaim/', type='http', auth='public', method='GET')
    def get_claim(self, **kwargs):
        Claims = http.request.env['medical.insurance.claim']
        d = []
        claims = Claims.sudo().search([('name', '=', kwargs['cl'])])

        for claim in claims:
            d.append({
                      'name': claim.name,
                      'price_plan': claim.price_plan,
                      'contribution_charge' : claim.contribution_charge
                      })
        return json.dumps({'data': d})


    def update_claim(self, price_plan):

        data = request.httprequest.data
        res = json.loads(data)
        request.env['medical.insurance.claim'].sudo().write({
            price_plan: res['price_plan'],
            'contribution_charge': res['contribution_charge'],
        })











