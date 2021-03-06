# -*- coding: utf-8 -*-
{
    'name': "library",

    'summary': """
        This module is for studying only. There is nothing particular about it!""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Tam Nguyen",
    'website': "no website",
    'application': True,


    'category': 'Uncategorized',
    'version': '0.1',


    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/library_view.xml',
        'views/book_view.xml',
        'views/css_loader.xml',
        'views/book_list_template.xml',
        'views/partner_list_template.xml',
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'reports/library_book_reports.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'post_init_hook': '_register_hook',
}
