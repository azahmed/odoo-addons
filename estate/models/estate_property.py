# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tools import date_utils
from odoo import fields, models
today = fields.Datetime.now()

class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Estate Property Description"

    name = fields.Char(required=True, default="unknow")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=date_utils.add(today, months=3))
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
            string='Type',
            selection=[('north', 'North'), ('south', 'South')],
            help="Type is used to separate Leads and Opoo")

    state = fields.Selection(
            string='State',
            selection=[('New', 'New'), ('Offer Received', 'Offer Received'), ('Offer Accepted', 'Offer Accepted'), ('Sold', 'Sold'), ('Cancelled', 'Cancelled')],
            help="States, should not be deitable",
            required=True,
            default='New',
            copy=False)
    active = fields.Boolean(default=True)
    partner_id = fields.Many2one("res.partner", string="Partner")
    property_type_id = fields.Many2one("estate_property_type", string="Property Type")