# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Solicitud(models.Model):
        _name = 'solcomp'

        name_id = fields.Many2one('produc',string="Nombre",required= True)
        cant= fields.Integer(string="Cantidad",required= True)
        date_solicitud = fields.Date('Fecha de solicitud', default=fields.Date.context_today, readonly=True, select=True)
        estado = fields.Selection(string='Estado', selection=[('a', 'Pedido pendiente'),
                                                            ('b', 'Pedido realizado'), 
                                                            ('c', 'Pedido recibido'),
                                                            ('d', 'Ingresado a inventario'),
                                                            ],
                                default="a", track_visibility='onchange', required= True )
        
        obs= fields.Text(string="Observaciones")
