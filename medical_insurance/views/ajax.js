odoo.define('medical_insurance./medical_insurance/createclaim/', function (require) {

    "use strict";
    // Odoo class to calling an url with JSONRPC
    var ajax = require('web.ajax');
    $(this).on("click", ".submit", function () {
        /// Call URL /update_partner with jsonRpc with attribute name, address, country
        ajax.jsonRpc("/update_patner", 'call', {'patient_id': patient_id,
            'medical_center_id': medical_center_id,
            'service_line_id':service_line_id,
            'visit_type':visit_type})

            .then(function (data) {
                  // Action after update
             });
        })
    }