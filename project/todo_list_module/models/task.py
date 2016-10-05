# -*- coding: utf-8 -*-
# Copyright (C) 2009-2016 Trobz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class Task(models.Model):
    _name = "task"
    _inherit = ['mail.thread']
    _description = "TODO"
    _order = "stage_seq, sequence, priority desc"

    id = fields.Integer('ID', readonly=True)
    name = fields.Char('Summary', index=True, required=True)
    description = fields.Text('Description')
    sequence = fields.Integer('Sequence', default=16, index=True)
    date_deadline = fields.Date('Due Date')
    priority = fields.Selection(
        (('1', 'Low'), ('2', 'Normal'),
         ('3', 'High'), ('4', 'Urgent')), 'Priority', default='2')
    active = fields.Boolean('Active', default=True)

    assignee_id = fields.Many2one('res.users', 'Assigned To', index=True,
                                  ondelete='set null')
    stage_id = fields.Many2one('task.stage', 'Stage', index=True,
                               default='_default_stage_id', required=True,
                               ondelete='restrict')
    tag_ids = fields.Many2many('task.tag', 'task_tag_rel', 'task_id', 'tag_id',
                               'Tags')

    stage_seq = fields.Integer('Stage Sequence', related='stage_id.sequence',
                               store=True)
