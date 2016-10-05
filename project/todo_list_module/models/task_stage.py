# -*- coding: utf-8 -*-
# Copyright (C) 2009-2016 Trobz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class TaskStage(models.Model):
    _name = "task.stage"
    _description = "Task Stage"
    _order = "sequence"

    name = fields.Char('Stage Name', index=True, required=True)
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
        for stage in self:
            stage.task_count = task_env.search(
                [('stage_id', '=', stage.id)], count=True)
        return

    @api.multi
    def view_related_tasks(self):
        """
        Display the related tasks of given stages.
        """
        action = self.env.ref('todo_list_module.action_all_tasks').read()
        tasks = self.env['task'].search([('stage_id', 'in', self.ids)])
        action[0].update({'domain': [('id', 'in', tasks.ids)]})
        return action[0]
