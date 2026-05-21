# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tools import date_utils, float_is_zero, float_compare
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
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
            string='Orientation',
            selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
            help="Which way does the garden face?")

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

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0.0)', 'Expected Price should be more than 0'),
        ('check_selling_price', 'CHECK(selling_price > 0.0)', 'Selling Price should be more than 0')
    ]

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            try:
                record.best_price = max(record.mapped("offer_ids.price"))
            except ValueError:
                record.best_price = 0

    @api.onchange("garden_orientation")
    def _onchange_garden_orientation(self):
        self.garden_area = 666

    @api.onchange("garden_area")
    def _onchange_garden_area(self):
        self.garden_orientation = "north"

    def action_estate_property_sold(self):
        for record in self:
            record.name = record.name + "Sold"
            if record.state == 'Sold':
                raise UserError("Already Sold")
            if record.state == 'Cancelled':
                raise UserError("Cannot sell, already Cancelled")

        return True

    def action_estate_property_cancelled(self):
        for record in self:
            record.name = record.name + "Cancelled"
            if record.state == 'Sold':
                raise UserError("Already Sold, Cannot be Cancelled")
        return True

    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if float_is_zero(record.selling_price, precision_digits=2):
                raise ValidationError("Selling Price cannot be zero")
            print("This is Asrar", "asrar")
            print("selling_price:", record.selling_price, "percentage:", record.selling_price*.9, "diff:", float_compare(record.selling_price, record.selling_price*.9, precision_digits=2))
            if float_compare(record.selling_price, record.selling_price*.9, precision_digits=2) >=0 :
                raise ValidationError("Some percentage error")

# any(not float_is_zero(bom_line.cost_share, precision_digits=2) for bom_line in variant_bom_lines),