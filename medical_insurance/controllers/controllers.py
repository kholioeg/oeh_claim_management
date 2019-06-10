# -*- coding: utf-8 -*-
# from odoo import http


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
            return '{"response": "this claim is not valid"}'

        return {
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






