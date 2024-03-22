# -*- coding: utf-8 -*-
{
    'name': "serah_listing",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale.xml',
        'views/account.xml',
        'views/stock.xml',
        'views/listing.xml',
        'views/mail_form.xml',
        'views/menu.xml',
        'report/report.xml',
        'report/template.xml',
        'template/mail_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
