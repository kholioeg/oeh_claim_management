# -*- coding: utf-8 -*-
from odoo import http
from odoo.tools.translate import _
from odoo.http import request

class MedicalInsurance(http.Controller):
    @http.route('/medical_insurance/medical_insurance/', type='http', auth='public', methods=['GET'])
    def index(self, **kw):
        return "Hello, world"

    @http.route('/medical_insurance/medical_insurance/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('medical_insurance.listing', {
            'root': '/medical_insurance/medical_insurance',
            'objects': http.request.env['medical_insurance.medical_insurance'].search([]),
        })

    @http.route('/medical_insurance/medical_insurance/objects/<model("medical_insurance.medical_insurance"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('medical_insurance.object', {
            'object': obj
        })