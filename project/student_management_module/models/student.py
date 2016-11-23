
from openerp import models, fields


class Student(models.Model):
    _name = 'student'
    _description = 'Student'
    _order = 'id_student'

    name = fields.Char(
        string="Name",
        index=True,
        required=True
    )
    id_student = fields.Char(
        string="Student ID",
        required=True
    )
    gender = fields.Selection(
        selection=(('male', 'Male'), ('female', 'Female'),
                   ('other', 'Other')),
        string="Gender",
        required=True
    )
    image = fields.Binary(string="Image")
    birthday = fields.Date(string="Date of Birth")
    note = fields.Text(string="Internal Notes")
