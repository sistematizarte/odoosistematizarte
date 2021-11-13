# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PaymentRegister(models.Model):
   _inherit = "account.payment.register"

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


