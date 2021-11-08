# -*- coding: utf-8 -*-
from odoo import fields, models


class MyCRMPorter(models.Model):
    _name = "my_crm.porter"
    _description = "My CRM Porter"

    units_number = fields.Integer("Units Number", help="Quantity of units")
    blocks_number = fields.Integer("Blocks Number", help="Quantity of blocks")
    residents_number = fields.Integer("Residents Number", help="Quantity of residents")
    porter_type = fields.Selection([
        ('own', 'Own'),
        ('outsourced', 'Outsourced')
    ], required=True, default='own',
        help="own or outsourced.")
    porter_time = fields.Selection([
        ('duration_24_hours', 'Duration24Hours'),
        ('duration_12_hours', 'Duration12Hours')
    ], required=True, default='duration_24_hours',
        help="24hrs or 12hrs.")
