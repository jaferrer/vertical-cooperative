# -*- coding: utf-8 -*-

# Copyright 2018 Rémy Taymans <remytaymans@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Easy My Coop Website Portal',

    'summary': """
    Show cooperator information in the website portal.
    """,
    'description': """
    """,

    'author': 'Rémy Taymans',
    'license': 'AGPL-3',
    'version': '9.0.1.0',
    'website': "www.coopiteasy.be",

    'category': 'Website, Cooperative Management',

    'depends': [
        'website',
        'website_portal_v10',
        'easy_my_coop',
        'report',
    ],

    'data': [
        'views/easy_my_coop_website_portal_templates.xml',
    ]
}