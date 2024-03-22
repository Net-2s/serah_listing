# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
import pytz



class SerahListing(models.Model):
    _name = 'serah.listing'
    _description = 'serah.listing'

    def _get_name(self):
        tz = pytz.timezone('Europe/Paris') 
        now = datetime.now(tz)
        date = now.strftime("%Y-%m-%d")
        hour = now.strftime("%H")
        minutes = now.strftime("%M")

        return f'SERAH IN - {date} - [{hour}:{minutes}] '
    
    name = fields.Char(
        string="Titre", default=_get_name)
    
    listing_line = fields.One2many(
        comodel_name='serah.listing.line',
        inverse_name='listing_id',
        string="Liste des Articles",
        copy=True, auto_join=True)

    def action_quotation_send(self):
        # lang = self.env.context.get('lang')
        mail_template = self.env.ref('serah_listing.email_template_serah_in_id', raise_if_not_found=False)
        ctx = {
            'default_model': 'serah.listing',
            'default_res_id': self.id,
            'default_use_template': bool(mail_template),
            'default_template_id': mail_template.id if mail_template else None,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'default_email_layout_xmlid': 'mail.mail_notification_layout_with_responsible_signature',
            # 'proforma': self.env.context.get('proforma', False),
            'force_email': True,
            'model_description': "Listing",
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }



class SerahListingLine(models.Model):
    _name = 'serah.listing.line'
    _description = 'serah.listing.line'

    note = fields.Char(
        string="Note")
    
    listing_id = fields.Many2one(
        comodel_name='serah.listing',
        string="Liste",
        required=True, ondelete='cascade')
    
    product_id = fields.Many2one(
        comodel_name='product.product',
        string="Article", required=True)
    
    price_unit = fields.Float(
        string="Prix Unitaire",
        readonly=False, required=True)
    
    quantity = fields.Float(
        string='Quantité', 
        compute="_compute_quantity", 
        readonly=False)
    
    barcode = fields.Char(
        string='Code-barres', 
        compute="_compute_code_barres")
    
    texte = fields.Char(
        string='Texte', 
        compute="_compute_texte",
        readonly=False)
    
    colissage = fields.Float(
        string='Colissage', 
        compute="_compute_colissage")
    
    image_1920 = fields.Binary(
        string='Image', 
        compute="_compute_image")

    @api.depends('product_id')
    def _compute_code_barres(self):
        for record in self:
            record.barcode = record.product_id.barcode
    
    @api.depends('product_id')
    def _compute_image(self):
        for record in self:
            record.image_1920 = record.product_id.image_1920

    @api.depends('product_id')
    def _compute_texte(self):
        for record in self:
            record.texte = record.product_id.texte

    @api.depends('product_id')
    def _compute_colissage(self):
        for record in self:
            record.colissage = record.product_id.colissage

    @api.depends('product_id')
    def _compute_quantity(self):
        for record in self:
            qty =  record.product_id.qty_available
            record.quantity = qty > 0 and qty or 1



