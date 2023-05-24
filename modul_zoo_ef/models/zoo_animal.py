import string
from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    continentOrigen = fields.Char('Continent Origen')
    dataNaix = fields.Date('Data de naixament')
    paisOrigen = fields.Char('Pais Origen')
    sexe = fields.Char('Sexe')
    
    zoo_id = fields.Many2one('zoo.zoo', string='Zoo')
    especie_id = fields.Many2one('zoo.especie', string='Especie')