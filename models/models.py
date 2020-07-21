from odoo import models, fields, api, _
from odoo.exceptions import UserError

import odoo.addons.decimal_precision as dp

class StockMove(models.Model):
    _inherit = 'stock.move'

    standard_price = fields.Float(compute='get_standard_price', string='Cost')
    
    def get_standard_price(self):
        for line in self:
            line.standard_price = line.product_id.standard_price
        return
    

    # standard_price = fields.Float(
    #     'Cost',
    #     inverse='_set_standard_price', search='_search_standard_price',
    #     digits=dp.get_precision('Product Price'), groups="base.group_user",
    #     help="Cost of the product, in the default unit of measure of the product.")

    # @api.depends('product_variant_ids', 'product_variant_ids.standard_price')
    # def _compute_standard_price(self):
    #     unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
    #     for template in unique_variants:
    #         template.standard_price = template.product_variant_ids.standard_price
    #     for template in (self - unique_variants):
    #         template.standard_price = 0.0

    # @api.one
    # def _set_standard_price(self):
    #     if len(self.product_variant_ids) == 1:
    #         self.product_variant_ids.standard_price = self.standard_price
    
    # def _search_standard_price(self, operator, value):
    #     products = self.env['product.product'].search([('standard_price', operator, value)], limit=None)
    #     return [('id', 'in', products.mapped('product_tmpl_id').ids)]

class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    standard_price = fields.Float(compute='get_standard_price', string='Cost')
    
    @api.depends('product_qty')
    def get_standard_price(self):
        for line in self:
            line.standard_price = line.product_qty * line.product_id.standard_price
        return

    # standard_price = fields.Float(
    #     'Cost',
    #     inverse='_set_standard_price', search='_search_standard_price',
    #     digits=dp.get_precision('Product Price'), groups="base.group_user",
    #     help="Cost of the product, in the default unit of measure of the product.")
        
    # @api.one
    # def _set_standard_price(self):
    #     if len(self.product_variant_ids) == 1:
    #         self.product_variant_ids.standard_price = self.standard_price

    # @api.depends('product_variant_ids', 'product_variant_ids.standard_price')
    # def _compute_standard_price(self):
    #     unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
    #     for template in unique_variants:
    #         template.standard_price = template.product_variant_ids.standard_price
    #     for template in (self - unique_variants):
    #         template.standard_price = 0.0

    # def _search_standard_price(self, operator, value):
    #     products = self.env['product.product'].search([('standard_price', operator, value)], limit=None)
    #     return [('id', 'in', products.mapped('product_tmpl_id').ids)]