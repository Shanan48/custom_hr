# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HRHR(models.Model):
    _name = 'hr.hr'

    name = fields.Char(string="Employee Name", required=True, )
    birth_date = fields.Date(string="Date of Birth")
    age = fields.Float(string="Age", compute="_compute_age")
    salary = fields.Integer(string="Salary", help="Add Salary here")


    @api.depends('birth_date')
    def _compute_age(self):
        self.age = 35.3


class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    num_xyz = fields.Float(string="Num XYZ",  required=False, )


# class YZOrder(models.Model):
#     _name = 'yz.order'
#     _inherit = 'sale.order'
#
#     name = fields.Char()
