{
    'name': 'Library Management',
    'version': '13.0.1.0',
    'category': 'Tools',
    'author': 'Odoo Mates',
    'website': 'odoomates.com',
    'license': 'AGPL-3',
    'summary': 'Library management',
    'description': """Module to manage Library""",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/books.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False

}