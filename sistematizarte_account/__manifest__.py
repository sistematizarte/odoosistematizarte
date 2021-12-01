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
    'depends': [ 'base', 'account', 'sale', 'project', 'hr_expense'],
    'data': [
        'views/tree_views.xml',
        'views/menu_views.xml',
        'segurity/datos_segurity.xml',
        'segurity/ir.model.access.csv',
    ],
    'application': False,
    'installable': True,
}