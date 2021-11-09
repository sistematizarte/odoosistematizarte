# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# -*- coding: utf-8 -*-
{
    'name': 'sistematizarte | Contabilidad',
    'description': ''' Projecto Contabilidad ''',
    "version": "14.0.1.0.0",
    "author": "",
    "website": "",
    'category': 'account',
    'depends': [ 'base', 'account', 'sale' ],
    'data': [
        'views/menu_views.xml',
        'segurity/datos_segurity.xml',
        'segurity/ir.model.access.csv',
        'views/tree_views.xml',
    ],
    'application': False,
    'installable': True,
}