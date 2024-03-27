# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ReportSerahListing(models.AbstractModel):
    _name = 'report.serah_listing.report_listing'
    _description = 'Get Serah Listing as PDF.'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['serah.listing'].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': 'serah.listing',
            'docs': docs,
        }
