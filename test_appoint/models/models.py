# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class test_appoint(models.Model):
#     _name = 'test_appoint.test_appoint'
#     _description = 'test_appoint.test_appoint'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
