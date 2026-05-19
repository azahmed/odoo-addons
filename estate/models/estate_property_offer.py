# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from email.policy import default

from odoo import api, fields, models
from pkg_resources import require
today = fields.Datetime.now()


class EstatePropertyOffer(models.Model):
    _name = "estate_property_offer"
    _description = "Estate Property Offer"

    price = fields.Float(required=True, string='YaPrice')
    status = fields.Selection(
        string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help="Refused or Accepted")
    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate_property", string="Property", required=True)
    validity = fields.Integer(default=7)
    # date_deadline = fields.Date(compute="_inverse_date_deadline")
    date_deadline = fields.Date()

    # @api.depends("create_date", "validity")
    # def _inverse_date_deadline(self):
    #     for record in self:
    #         if record.create_date is None:
    #             record.date_deadline = today + record.validity
    #         else:
    #             record.date_deadline = record.create_date + record.validity