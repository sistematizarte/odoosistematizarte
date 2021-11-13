# -*- coding: utf-8 -*-
{
    'name': 'sistematizarte | Finanzas',
    'description': ''' Proyecto Contabilidad ''',
    "version": "14.0.1.0.0",
    "author": "",
    "website": "",
    'category': 'account',
    'depends': ['base', 'account', 'sale'],
    'data': [
        'views/finance_custom.xml',
        'views/budget_custom.xml',
        'views/payment_custom.xml',
    ],
    'application': False,
    'installable': True,
}