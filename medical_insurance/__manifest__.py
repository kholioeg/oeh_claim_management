# -*- coding: utf-8 -*-
{
    'name': "medical_insurance",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'portal', 'product', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/patient.xml',
        'views/claim.xml',
        'views/serviceline.xml',
        'views/priceplan.xml',
        'views/medicalcenter.xml',
        'views/ehr.xml',
        'views/price_plan_report.xml',
        'views/patient_report.xml',
        'views/medical_center_report.xml',
        'views/disease.xml',
        'views/vital_signs_history.xml',
        'views/operation_reservation.xml',
        'views/doctors.xml',
        'views/room.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}