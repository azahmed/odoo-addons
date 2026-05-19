# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class EstatePropertyOffer(models.Model):
    _name = "estate_property_offer"
    _description = "Estate Property Offer"

    price = fields.Float(required=True, string='YaPrice')
    status = fields.Selection(
        string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help="Refused or Accepted")
    # partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate_property", string="Property")

    #property_ids = fields.One2many('estate.property', 'property_type_id', string='Materials')