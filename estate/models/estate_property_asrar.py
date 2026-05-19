# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class EstatePropertyAsrar(models.Model):
    _name = "estate_property_asrar"
    _description = "Estate Property Asrar"

    name = fields.Char(required=True)
    gender = fields.Char(required=True)

    #property_ids = fields.One2many('estate.property', 'property_type_id', string='Materials')