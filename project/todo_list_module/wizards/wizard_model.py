# -*- coding: utf-8 -*-
# Copyright (C) 2009-2016 Trobz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class WizardModel(models.TransientModel):
    _name = "module.wizard_model"

    @api.multi
    def action_accept(self):
        self.ensure_one()
        self.do_something_useful()
