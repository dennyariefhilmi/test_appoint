# -*- coding: utf-8 -*-
# from odoo import http


# class TestAppoint(http.Controller):
#     @http.route('/test_appoint/test_appoint/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_appoint/test_appoint/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_appoint.listing', {
#             'root': '/test_appoint/test_appoint',
#             'objects': http.request.env['test_appoint.test_appoint'].search([]),
#         })

#     @http.route('/test_appoint/test_appoint/objects/<model("test_appoint.test_appoint"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_appoint.object', {
#             'object': obj
#         })
