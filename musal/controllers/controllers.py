# -*- coding: utf-8 -*-
from odoo import http

# class Musal(http.Controller):
#     @http.route('/musal/musal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/musal/musal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('musal.listing', {
#             'root': '/musal/musal',
#             'objects': http.request.env['musal.musal'].search([]),
#         })

#     @http.route('/musal/musal/objects/<model("musal.musal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('musal.object', {
#             'object': obj
#         })