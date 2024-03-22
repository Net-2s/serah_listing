# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductInherit(models.Model):
    _inherit = 'product.template'


    barcode = fields.Char('Barcode', compute='_compute_barcode', inverse='_set_barcode', search='_search_barcode', required=True)
    
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         if vals['barcode']:
    #             products = self.env['product.template'].search([('barcode', '=', vals['barcode'])])
    #             if len(products) > 0:
    #                 ValidationError(f"Le code barre [{vals['barcode']}] est déjà utilisé pour un autre produit. Sélectionnez un autre !")
    #     return super(ProductInherit, self).create(vals_list)
    
    # def write(self, vals):
    #     if vals['barcode']:
    #         products = self.env['product.template'].search([('barcode', '=', vals['barcode'])])
    #         if len(products) > 0:
    #             ValidationError(f"Le code barre [{vals['barcode']}] est déjà utilisé pour un autre produit. Sélectionnez un autre !")
    #     return super(ProductInherit, self).write(vals)
         

