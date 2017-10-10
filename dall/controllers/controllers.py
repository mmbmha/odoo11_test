# -*- coding: utf-8 -*-
from odoo import http

# class Dall(http.Controller):
#     @http.route('/dall/dall/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dall/dall/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dall.listing', {
#             'root': '/dall/dall',
#             'objects': http.request.env['dall.dall'].search([]),
#         })

#     @http.route('/dall/dall/objects/<model("dall.dall"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dall.object', {
#             'object': obj
#         })