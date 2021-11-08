# -*- coding: utf-8 -*-
from odoo import fields, models


class PorterTeam(models.Model):
    _inherit = "crm.lead"

    units_number = fields.Integer("Units Number", help="Quantity of units")
    blocks_number = fields.Integer("Blocks Number", help="Quantity of blocks")
    residents_number = fields.Integer("Residents Number", help="Quantity of residents")
    porter_type = fields.Selection([
        ('own', 'Own'),
        ('outsourced', 'Outsourced')
    ], required=True, default='own',
        help="own or outsourced.")
    porter_time = fields.Selection([
        ('24_hours', '24Hours'),
        ('12_hours', '12Hours')
    ], required=True, default='duration_24_hours',
        help="24hrs or 12hrs.")
