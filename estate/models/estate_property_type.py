# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate_property_type"
    _description = "Estate Property Type Description"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)

    #property_ids = fields.One2many('estate.property', 'property_type_id', string='Materials')