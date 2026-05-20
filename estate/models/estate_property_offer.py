# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from email.policy import default

from odoo import api, fields, models
from pkg_resources import require
from datetime import datetime, timedelta
from odoo.exceptions import UserError
today = fields.Datetime.now()


class EstatePropertyOffer(models.Model):
    _name = "estate_property_offer"
    _description = "Estate Property Offer"

    price = fields.Float(required=True, string='YaPrice')
    status = fields.Selection(
        string='Status',
        selection=[('new', 'New'), ('accepted', 'Accepted'), ('refused', 'Refused')],
        help="Refused or Accepted")
    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate_property", string="Property", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    # date_deadline = fields.Date()

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            if not record.create_date:
                record.date_deadline = today + timedelta(record.validity)
            else:
                record.date_deadline = record.create_date + timedelta(record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - today.date()).days

    def action_estate_offer_confirm(self):
        for record in self:
            raise UserError("Confirming Mate")

        return True
