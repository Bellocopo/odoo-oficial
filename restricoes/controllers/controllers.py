# -*- coding: utf-8 -*-
from odoo import http

class MyModule(http.Controller):
    @http.route('/restricoes/restricoes/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/restricoes/restricoes/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('restricoes.listing', {
            'root': '/restricoes/restricoes',
            'objects': http.request.env['restricoes.restricoes'].search([]),
        })

    @http.route('/restricoes/restricoes/objects/<model("restricoes.restricoes"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('restricoes.object', {
            'object': obj
        })