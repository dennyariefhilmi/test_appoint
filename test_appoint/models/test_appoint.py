from odoo import fields, models, api


class test_appoint(models.Model):
    _name = 'test.appoint'
    _description = 'Description'

    name = fields.Char()
    appointment_name = fields.Char(
        string='Appointment Name',
        required=True)
    appointment_date = fields.Date(
        string='Appointment Date',
        required=True,
        default=fields.Date.today())
    private_appointment = fields.Boolean(
        string='Private Appointment',
        required=True)
    appointment_type = fields.Selection(
        string='Appointment Type',
        selection=[('self', 'Self'),
                   ('company', 'Company'), ],
        required=True, )
    company = fields.Many2one(
        comodel_name='res.company',
        string='Company Name',
        required=True)

    email = fields.Char(
        string='Email Company',
        required=True)

    user = fields.Many2one(
        comodel_name='res.users',
        string='User in Charge',
        required=True)

