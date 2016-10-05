# -*- coding: utf-8 -*-
# Copyright (C) 2009-2016 Trobz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.tools.translate import _


class TaskTag(models.Model):
    _name = "task.tag"
    _description = "Task Stage"
    _order = "sequence"

    name = fields.Char('Tag Name', index=True, required=True)
    description = fields.Text('Description')
    sequence = fields.Integer('Sequence', default=16, index=True)
    active = fields.Boolean('Active', default=True)

    task_count = fields.Integer('Tasks Count', compute='_compute_task_count')

    @api.multi
    def _compute_task_count(self):
        """
        Count the number of related tasks of given tags.
        """
        task_env = self.env['task']
        for tag in self:
            tag.task_count = task_env.search(
                [('tag_ids', 'in', [tag.id])], count=True)
        return

    @api.multi
    def view_related_tasks(self):
        """
        Display the related tasks of given tags.
        """
        action = self.env.ref('todo_list_module.action_all_tasks').read()
        tasks = self.env['task'].search([('tag_ids', 'in', self.ids)])
        action[0].update({'domain': [('id', 'in', tasks.ids)]})
        return action[0]
