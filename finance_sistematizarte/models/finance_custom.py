from odoo import models, fields, api

class FinanceOdoo(models.Model):
    _inherit = 'account.move'

    project = fields.Many2one('project.project', string='Proyecto')
    select_payment = fields.Selection([("payment_budget", "Anticipo"), ("payment_first_share", "Primera Cuota"),
            ("payment_second_share", "Segunda Cuota"), ("paymen_total", "Pago Total"), ("payment_partial", "Pago Complementario"),
            ("paynment_monthy", "Pago Mensual"),], default="payment_budget", string="Cuota de Pago",)
    total = fields.Float(compute='_total_ganado')

    def _total_ganado(self):
        # total_id = self.env['amount_total']
         total = self['amount_total']
         self.total = total

class Presupuesto(models.Model):
    _inherit = 'sale.order'

    project = fields.Many2one('project.project', string='Proyecto')
    # total = fields.Float(compute='_total_ganado')

    # def _total_ganado(self):

        # #total = self.env['amount_total']
        # total_id = self.env['account.move'].search([('amount_total_signed')])
        # self.total = total_id

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    project = fields.Many2one('project.project', string='Proyecto')
    select_payment = fields.Selection(
        [
            ("payment_budget", "Anticipo"),
            ("payment_first_share", "Primera Cuota"),
            ("payment_second_share", "Segunda Cuota"),
            ("paymen_third_total", "Pago Total"),
            ("payment_partial", "Pago Complementario"),
            ("paynment_monthy", "Pago Mensual"),
        ],
        default="payment_budget",
        string="Cuota de Pago",
    )
