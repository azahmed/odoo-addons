# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _

class EstatePropertyTag(models.Model):
    _name = "estate_property_tag"
    _description = "Estate Property Tag"

    name = fields.Char(required=True)
    doda = fields.Char()

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'Cannot repeat tags Dumb Ass!')
    ]

    #property_ids = fields.One2many('estate.property', 'property_type_id', string='Materials')