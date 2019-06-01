from odoo import models, fields, api,tools


class Patient(models.Model):
    _name = 'medical.insurance.patient'
    _inherit = 'res.partner'

    name = fields.Char(string="patient no", readonly=True)
    first_name = fields.Char(string="First name")
    last_name = fields.Char(string="Last name")
    image = fields.Binary()
    NID = fields.Char(string='NID')
    date_of_birth = fields.Date(string='Birth date')
    gender = fields.Selection([
        ('male', "Male"),
        ('female', "Female"),
    ])

    marital_status = fields.Selection([
        ('single', "Single"),
        ('married', "Married"),
    ], default="single")
    blood_group = fields.Char(string='blood group')
    weight = fields.Float()
    height = fields.Float()
    status = fields.Boolean()
    patient_line = fields.One2many('medical.insurance.patient.line', inverse_name="name", string="patient line", required=True)
    EHR = fields.One2many('medical.insurance.ehr', inverse_name="patient_id", string="EHR", required=True)

    # @api.multi
    # @api.depends('image')
    # def _get_image(self):
    #     for rec in self:
    #         rec.image = tools.image_resize_image_medium(
    #             rec.image, size=(100, 100))

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('medical.insurance.patient') or '/'
        vals['name'] = seq
<<<<<<< Updated upstream
        return super(Patient, self).create(vals)
=======
        return super(Patient, self).create(vals)


    @api.multi
    @api.onchange('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday and record.birthday <= fields.Date.today():
                record.age = relativedelta(
                    fields.Date.from_string(fields.Date.today()),
                    fields.Date.from_string(record.birthday)).years
            else:
                record.age = 0


# @api.multi
# def name_get(self, cr, uid, ids, context=None):
#     if context is None:
#         context = {}
#         res = []
#         for record in self.browse(cr, uid, ids, context=context):
#             mrn = record.name
#             patient = record.first_name
#             tit = "%s <%s>" % (mrn, patient)
#             res.append((record.id, tit))
#         return res


# @api.one
# @api.depends('name', 'first_name')
# def _compute_display_name(self):
#     names = [self.first_name, self.name]
#     self.display_name = ' / '.join(filter(None, names))
#
# @api.multi
# def name_get(self, cr, uid, ids, context=None):
#     if not ids:
#         return []
#     reads = self.read(cr, uid, ids, ['first_name', 'name'], context=context)
#     res = []
#     for record in reads:
#         name = record['first_name']
#         if record['name']:
#             name = record['name'][1] + ' / ' + name
#         res.append((record['id'], name))
#     return res





def name_get(self, cr, uid, ids, context=None):
    if not ids:
        return []
    reads = self.read(cr, uid, ids, ['name','first_name'], context=context)
    res = []
    for record in reads:
        name = record['name']
        if record['first_name']:
            name = record['first_name'][1]+' / '+name
        res.append((record['id'], name))
    return res
>>>>>>> Stashed changes
