# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tools import date_utils
from odoo import api, fields, models
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
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    salesPerson_id = fields.Many2one("res.users", string="Seller", default=lambda self: self.env.user)
    property_type_id = fields.Many2one("estate_property_type", string="Property Type")
    tag_ids = fields.Many2many('estate_property_tag', string='Tags')
    offer_ids = fields.One2many('estate_property_offer', 'property_id', string='Offers')
    total_area = fields.Float(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.mapped("offer_ids.price"))