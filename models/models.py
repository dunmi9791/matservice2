# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VehicleMatservice(models.Model):
    _name = 'vehicle.matservice'
    _rec_name = 'vin_no'
    _description = 'Vehicles'

    make = fields.Char(string="Make")
    vehicle_model = fields.Char(string="Model")
    year = fields.Char(string="Year")
    colour = fields.Char(string="Colour")
    vin_no = fields.Char(string="Vin Number")
    reg = fields.Char(string="Registration Number")
    quotes_ids = fields.One2many(comodel_name="sale.order", inverse_name="vehicle_id", string="Quotes", required=False, )
    owner_id = fields.Many2one(comodel_name="res.partner", string="", required=False, )


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    vehicle_id = fields.Many2one(comodel_name="vehicle.matservice", string="Vehicle", required=False, )
    make = fields.Char(related="vehicle_id.make")
    vehicle_model = fields.Char(related="vehicle_id.vehicle_model")
    year = fields.Char(related="vehicle_id.year")
    colour = fields.Char(related="vehicle_id.colour")
    reg = fields.Char(related="vehicle_id.reg")
    amount_tax = fields.Monetary(string='VAT', store=True, readonly=True, compute='_amount_all')

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            vehicle_ids = self.partner_id.vehicle_ids.ids
            return {'domain': {'vehicle_id': [('id', 'in', vehicle_ids)]}}


class Partner(models.Model):

    _inherit = 'res.partner'

    vehicle_ids = fields.One2many(comodel_name="vehicle.matservice", inverse_name="owner_id", string="Vehicles", required=False, )


# class matservice(models.Model):
#     _name = 'matservice.matservice'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
