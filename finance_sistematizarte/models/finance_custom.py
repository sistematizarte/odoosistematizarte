from odoo import models, fields, api

class FinanceOdoo(models.Model):
	_inherit = "account.move"

	project = fields.Many2one("project.project", string="Proyecto")