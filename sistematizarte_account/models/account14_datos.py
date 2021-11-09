from odoo import models, fields, api

class datos(models.Model):
    _name = 'datos' #NOMBRE DE LA TABLA
    _description = 'datos de contabilidad'

    numero = fields.Char(string='numero')
    proyecto = fields.Char(string='proyecto')
    pago = fields.Integer('pago')
    cliente = fields.Char('cliente')
    fecha = fields.Date('fecha')
    impuesto = fields.Integer('impuesto')
    estatus = fields.Boolean('estatus')
    estatus_p = fields.Boolean('estatus_p') #estado de pago

#class Sale_Custom(models.Model):
#    _inherit = "sale.order"
