# -*- coding: utf-8 -*-
from odoo import http
import odoo
import json

class Books(http.Controller):

    @http.route('/library/books', auth='user')
    def list(self, **kwargs):
        Book = http.request.env['library.book']
        books = Book.search([])
        return http.request.render(
            'library.book_list_template', {'books':books}
        )

    @http.route('/partners', auth='user')
    def list_2(self):
        Partners = http.request.env['res.partner'].search([])
        return http.request.render(
            'library.partner_list_template', {'partners':Partners}
        )

class PetHandler(http.Controller):

    @http.route('/json_test/<dbname>', auth='public', type='json', methods=['GET'], sitemap=False, cors='*', csrf=False)
    def list_3(self, dbname):
        model_name = 'res.partner'
        try:
            registry = odoo.modules.registry.Registry(dbname)
            with odoo.api.Environment.manage(), registry.cursor() as cr:
                env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
                rec = env[model_name].search([], limit=1)
                response = {
                    "status": "ok",
                    "content": {
                        "name": rec.name,
                    }
                }
        except Exception:
            response = {
                "status": "error",
                "content": "not found",
            }
        return json.dumps(response)
