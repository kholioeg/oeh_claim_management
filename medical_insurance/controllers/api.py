
from odoo import http
import json
import logging
from odoo.http import Response, request
_logger = logging.getLogger(__name__)


class Api(http.Controller):

    #patient routes
    @http.route('/api/medical_insurance/patients/', type='http', auth='public', method='GET')
    def medical_patient(self, **kw):
        patients = http.request.env['medical.insurance.patient']
        all_patients = []
        patient = patients.sudo().search([])
        for p in patient:
            all_patients.append({'id': p.id,
                                 'first name' : p.first_name,
                                 'last name' : p.first_name,
                                 'MRN': p.name,
                                 'NID' : p.NID,
                                 'age' : p.age,
                                 'gender' : p.gender,
                                 'marital status': p.marital_status
                                 })
        return json.dumps({'data': all_patients})


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



    # create claim
    @http.route('/api/medical_insurance/create_claim/', auth='public', methods=['POST'], type='json', csrf=False)
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
            return {"response": 403}

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



