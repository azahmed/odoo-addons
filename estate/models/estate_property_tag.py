# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _

class EstatePropertyTag(models.Model):
    _name = "estate_property_tag"
    _description = "Estate Property Tag"

    name = fields.Char(required=True)
    doda = fields.Char()

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'The name must be unique!')
    ]
    # _unique_name = models.Constraint(
    #     'UNIQUE(name)',
    #     'Cannot repeat tags Dumb Ass',
    # )
    # _sql_constraints = [
    #     ('unique_name', 'CHECK(percentage >= 0 AND percentage <= 100)',
    #      'The percentage of an analytic distribution should be between 0 and 100.')
    # ]
    #property_ids = fields.One2many('estate.property', 'property_type_id', string='Materials')