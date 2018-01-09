# -*- coding: utf-8 -*-
{
    'name': "Dall",

    'summary': """
        The first App on odoo11 by Dall""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dall.co",
    'website': "http://www.dall.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.21',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
