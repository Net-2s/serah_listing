from odoo import models, fields, api, _

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    barcode = fields.Char('Code-barres', compute="_compute_code_barres")
    texte = fields.Char('Texte', compute="_compute_texte")
    colissage = fields.Float('Colissage', compute="_compute_colissage")

    @api.depends('product_id')
    def _compute_code_barres(self):
        for record in self:
            record.barcode = record.product_id.barcode

    @api.depends('product_id')
    def _compute_texte(self):
        for record in self:
            record.texte = record.product_id.texte

    @api.depends('product_id')
    def _compute_colissage(self):
        for record in self:
            record.colissage = record.product_id.colissage