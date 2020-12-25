# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Categoria(models.Model):
    _name = 'cat'

    name= fields.Char(string="Categoría",required= True)
    
    encargado_cat=fields.Char(string="Encargado",required= True)
    
    categoria_ids= fields.One2many(
        'produc',
        'categoria_id',
        string='Productos')
    total_categorias = fields.Integer(string="total de productos", compute="_total_categorias")
    
    @api.one
    def _total_categorias(self):
        self.total_categorias =len(self.categoria_ids)   

    _sql_constraints = [('name', 'unique(name)', 'Esta categoría ya existe')
                        ]
    

class Productos(models.Model):
    _name = 'produc'
    
    name= fields.Char(string="Nombre",required= True)

    date_contract = fields.Date('Fecha de creación', default=fields.Date.context_today, readonly=True, select=True)
    
    stock = fields.Integer(string="Stock",required= True)
    stock_minimo = fields.Integer(string="Árticulos mínimo",required= True)
    stock_maximo = fields.Integer(string="Árticulos máximo")
  
    descripcion = fields.Text(string="Descripcion")
    
    estado_stock= fields.Text(string="Estado stock",compute="_estado_de_stock")

    categoria_id = fields.Many2one('cat',string="Categoría",required= True)
    
    imagen=fields.Binary(string="producto")

    _sql_constraints = [('name', 'unique(name)', 'Este producto ya existe')
                        ]

            
    
    @api.one
    def _estado_de_stock(self):
        if (self.stock <= self.stock_minimo):
            self.estado_stock= "Sin stock";
        else: self.estado_stock="Con stock";
        
    @api.constrains('stock')
    def _check_stock(self):
        for rec in self:
            if (rec.stock<0):
                raise ValidationError('El stock no puede ser negativo')
            
    @api.constrains('stock_minimo')
    def _check_stock_minimo(self):
        for rec in self:
            if (rec.stock_minimo<0):
                raise ValidationError('El stock mínimo no puede ser negativo')
            
            
    @api.constrains('stock_maximo')
    def _check_stock_maximo(self):

        for rec in self:
            if (rec.stock_maximo<0):
                raise ValidationError('El stock máximo no puede ser negativo')
            else: 
                if (rec.stock_maximo==0):
                    raise ValidationError('El stock máximo no puede 0')


