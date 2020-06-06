# -*- coding: utf-8 -*-
from odoo import http

class Books(http.Controller):

    @http.route('/library/books', auth='user')
    def list(self, **kwargs):
        Book = http.request.env['library.book']
        books = Book.search([])
        return http.request.render(
            'library.book_list_template', {'books':books}
        )

    @http.route('/partners', auth='user')
    def list(self):
        Partners = http.request.env['res.partner'].search([])
        return http.request.render(
            'library.partner_list_template', {'partners':Partners}
        )
