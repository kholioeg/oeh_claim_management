
from odoo import http
import json
import logging
from odoo.http import Response, request
_logger = logging.getLogger(__name__)


class Web(http.Controller):

#patient routes
#all patients
    @http.route('/web/medical_insurance/patients/', type='http', auth='public', method='GET')
    def medical_patient(self, **kw):
        patients = http.request.env['medical.insurance.patient']
        patient = patients.sudo().search([])
        return http.request.render('medical_insurance.all_patients', {
            'patients': patient
        })

#one patient
    @http.route('/web/medical_insurance/patient/', type='http', auth='public', method='GET')
    def patient_info_by_id(self, **kwargs):
        Patients = http.request.env['medical.insurance.patient']
        patient = Patients.sudo().search([('name', '=', kwargs['mrn'])])
        if patient:
            if patient.patient_status == 'Active':
                return http.request.render('medical_insurance.one_patient', {
                    'patient': patient
                })
            else:
                return http.request.render('medical_insurance.patient_Inactive', {})
        else:
            return http.request.render('medical_insurance.patient_notExist', {})

#create claim / web

    @http.route('/web/medical_insurance/claim/new/', type='http', auth="public", methods=['GET'], website=True)
    def get_create_claim_form(self, **kw):
        return http.request.render('medical_insurance.create', {})


    @http.route('/web/medical_insurance/create_claim/',type='http', auth='public', methods=['POST'], csrf=False)
    def webcreateclaim(self, **kw):
        new_patient = {
            'patient_id': kw['patient_id'],
            'medical_center_id': kw['medical_center_id'],
            'service_line_id': kw['service_line_id'],
            'visit_type': kw['visit_type']
        }
        #not valid claim temp
        claim = request.env['medical.insurance.claim'].sudo().create(new_patient)
        if claim.claim_status == 'Not Valid':
            return http.request.render('medical_insurance.notValid', {})

        return http.request.render('medical_insurance.claim_info', {
            'claims': claim
        })


    # update claim / web

    @http.route('/web/medical_insurance/claim/update/', type='http', auth="public", methods=['GET'], website=True)
    def get_update_claim_form(self, **kwargs):
        Claims = http.request.env['medical.insurance.claim']
        claims = Claims.sudo().search([('name', '=', kwargs['cl'])])
        return http.request.render('medical_insurance.update', {
            'claims': claims
        })


    @http.route('/web/medical_insurance/update_claim/', type='http', auth='public', methods=['POST'], csrf=False)
    def webupdateclaim(self, **kw):
        patient_id = kw['patient_id']
        center_id = kw['medical_center_id']
        service_id = kw['service_line_id']
        claim_id = kw['id']

        patient_obj = http.request.env['medical.insurance.patient'].sudo().search([('name', '=', patient_id)])
        center_obj = http.request.env['medical.insurance.medical.center'].sudo().search([('name', '=', center_id)])
        service_obj = http.request.env['medical.insurance.service.line'].sudo().search([('name', '=', service_id)])


        update_patient = {
            'patient_id': patient_obj.id,
            'medical_center_id': center_obj.id,
            'service_line_id': service_obj.id,
            'visit_type': kw['visit_type'],
            'id': claim_id
        }

        http.request.env['medical.insurance.claim'].sudo().search([('id', '=', claim_id )]).write(update_patient)
