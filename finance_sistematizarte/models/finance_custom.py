from odoo import models, fields, api

class FinanceOdoo(models.Model):
	_inherit = "account.move"
    
    #ingresos = fields.Monetary("account.move", "amount_total_signed" string="Ingresos")
    #ingresos = fields.Float('account.move')
    #egresos = fields.Float('account.move')
	project = fields.Many2one('project.project', string='Proyecto')
	select_payment =  fields.Selection(
        [
            ("payment_share", "Anticipo"),
            ("payment_first_share", "Primera Cuota"),
            ("payment_second_share", "Segunda Cuota"),
            ("paymen_third_total", "Pago Total"),
            ("payment_partial", "Pago Complementario"),
            ("paynment_monthy", "Pago Mensual"),
        ],
        default="payment_budget",
        string="Cuota de Pago",       
    )
    #ingresos_factur = fields.Float(string="Ingreso")

    #@api.depends('ingresos_factur')
    #def _calcular_fiels_account(self):
    #      ingresos = 0.0   
class Presupuesto(models.Model):
    _inherit = "sale.order"

    #refence_field = fields.Reference([('sale.order', 'amount_total')])
    project = fields.Many2one('project.project', string='Proyecto')

