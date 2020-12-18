# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'cat'

    name= fields.Char(string="Categoria",required= True)
    
    categoria_ids= fields.One2many(
        'produc',
        'categoria_id',
        string='Productos')
    total_categorias = fields.Integer(string="total de productos", compute="_total_categorias")
    
    @api.one
    def _total_categorias(self):
        self.total_categorias =len(self.categoria_ids)   


    

class Productos(models.Model):
    _name = 'produc'

    name= fields.Char(string="Nombre",required= True)
    date_contract = fields.Date('Fecha de creación', default=fields.Date.context_today, required=False, readonly=False, select=True)
    stock= fields.Integer(string="Stock",required= True)
    stock_minimo= fields.Integer(string="Árticulos minimos",required= True)
    stock_maximo= fields.Integer(string="Árticulos maximos",required= True)
    stock
    encargado= fields.Char(string="Encargado",required= True)
    descripcion= fields.Text(string="Descripcion")
    
    estado_stock= fields.Text(string="Estado stock",compute="_estado_de_stock")

    categoria_id = fields.Many2one('cat',string="Categoria",required= True)
    
    @api.one
    def _estado_de_stock(self):
        if (self.stock <= self.stock_minimo):
            self.estado_stock= "Sin stock";
        else: self.estado_stock="Con stock";
 
 



          

    

    

    




    
 







