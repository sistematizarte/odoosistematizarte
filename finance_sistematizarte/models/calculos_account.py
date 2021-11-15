from odoo import models, fields, api, _


class FinanceAccount(models.Model):
	_inherit = "account.move"

    total = fields.Float(compute='_total_ganado', string='Ganado')


