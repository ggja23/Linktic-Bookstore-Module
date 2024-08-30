# -*- coding: utf-8 -*-
{
    'name': "Linktic Bookstore Management",
    'summary': "Manage books, authors, and customers in a bookstore.",
    'description': "Manage books, authors, and customers in a bookstore.",
    'author': "Jhon Garcia",
    'category': 'Sales',
    'version': '17.1',
    'depends': ['base', 'mail'],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/author_views.xml',
        'views/customer_views.xml',
        'views/sale_order_line_views.xml',
        'views/sale_order_views.xml',
        'views/linktic_dashboard_view.xml',
        'views/actions.xml',
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'linktic_bookstore_management/static/src/js/linktic_dashboard.js',
            'linktic_bookstore_management/static/src/xml/linktic_dashboard_template.xml',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}

