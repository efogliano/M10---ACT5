from odoo import models, fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    name = fields.Char(compute='_get_name', string="Nom", readonly='True', store=False)
    nom = fields.Char('Nom')
    imatge = fields.Char('Imatge')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')
    latitud = fields.Float('Latitud')
    longitud = fields.Float('Longitud')

    desti_ids = fields.One2many('plane.vol','desti_id', string='Desti')
    origen_ids = fields.One2many('plane.vol','origen_id', string='Origen')

    def _get_name(self):
        for record in self:
            record.name = str(record.nom)