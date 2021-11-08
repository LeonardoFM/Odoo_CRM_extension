# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'My CRM',
    'version' : '1.1',
    'summary': 'Extends original CRM',
    'sequence': 10,
    'description': """Qualifying attributes: units, blocks, residents quantities, porter (own or outsourced) and time (24hrs or 12hrs)""",
    'category': 'Sales/CRM',
    'website': 'https://www.odoo.com/app/my_crm',
    'depends' : ['crm'],
    'data': [
        'views/lead_ext.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    #'post_init_hook': '_account_post_init',
    'assets': {
        'web._assets_primary_variables': [],
        'web.assets_backend': [],
        'web.assets_frontend': [],
        'web.assets_tests': [],
        'web.qunit_suite_tests': [],
        'web.assets_qweb': [],
    },
    'license': 'LGPL-3',
}
