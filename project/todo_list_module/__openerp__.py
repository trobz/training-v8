# -*- coding: utf-8 -*-
# Copyright (C) 2009-2016 Trobz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "TODOs List",
    "summary": "Simple TODOs List",
    "version": "8.0.1.0.1",
    "category": "Trobz Training",
    "website": "https://trobz.com/",
    "author": "Trobz",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "auto_install": False,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "mail"
    ],
    "data": [
        # data
        # security
        # wizards
        # views
        'views/task_stage_view.xml',
        'views/task_tag_view.xml',
        'views/task_view.xml',
        # reports
        # menus
        'views/task_menu.xml'
    ],
    "demo": [
        'demo/task_stage_demo.xml',
        'demo/task_tag_demo.xml',
        'demo/task_demo.xml',
    ],
    "css": ['static/src/js/*.css'],
    "js": ['static/src/js/*.js'],
    "qweb": ['static/src/js/*.xml']
}
