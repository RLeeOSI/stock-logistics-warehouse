# Copyright 2017-2020 ForgeFlow, S.L. (https://www.forgeflow.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    stock_request_ids = fields.One2many(
        comodel_name="stock.request",
        inverse_name="analytic_account_id",
        string="Stock Requests",
        copy=False,
    )
