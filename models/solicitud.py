# -*- coding: utf-8 -*-

from odoo import models, fields, api


        
class Solicitudes(models.Model):
    _name = 'solicitar'
    
    date_solicitar = fields.Date('Fecha de solicitud', default=fields.Date.context_today, readonly=True, select=True)

    solicitud_ids= fields.One2many(
       'solcomp',
       'solicitud_id',
        string='Solicitudes')