# -*- coding: utf-8 -*-
from odoo import http

# class Matservice(http.Controller):
#     @http.route('/matservice/matservice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/matservice/matservice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('matservice.listing', {
#             'root': '/matservice/matservice',
#             'objects': http.request.env['matservice.matservice'].search([]),
#         })

#     @http.route('/matservice/matservice/objects/<model("matservice.matservice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('matservice.object', {
#             'object': obj
#         })