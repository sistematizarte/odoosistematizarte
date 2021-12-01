import psycopg2 as psycopg2
from odoo import models, fields, api
import psycopg2


class datos(models.Model):
    _name = 'datos' #NOMBRE DE LA TABLA
    _description = 'datos de contabilidad'

    def _datos(self):
        for rec in self:
            rec.dato = self.env['account.move'].search('account_payment', '=', 'amount')
            rec.prueba = rec.dato
            return rec.prueba

    #def _get_default_name(self):
    #    dato = self.env['account.move'].search('account_payment', in, amount)
    #    self.prueba = dato
    #    return self.prueba

    prueba = fields.Char(
        string='Name',
        default=_datos,
    )


    project = fields.Many2one('project.project', string='Proyecto')
    account = fields.Many2one('account.move', string='Proveedores')
    total = fields.Float(string='total')


