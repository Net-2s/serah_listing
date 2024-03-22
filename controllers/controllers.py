# -*- coding: utf-8 -*-
# from odoo import http


# class SerahListing(http.Controller):
#     @http.route('/serah_listing/serah_listing', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/serah_listing/serah_listing/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('serah_listing.listing', {
#             'root': '/serah_listing/serah_listing',
#             'objects': http.request.env['serah_listing.serah_listing'].search([]),
#         })

#     @http.route('/serah_listing/serah_listing/objects/<model("serah_listing.serah_listing"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('serah_listing.object', {
#             'object': obj
#         })
