from odoo import models, fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    name = fields.Char(compute='_get_name',string='Nom Complet',readonly='true',store=False)
    imatge = fields.Char('Imatge')
    marca = fields.Char('Marca')
    model = fields.Char('Model')
    maxVel = fields.Float('Velocitat Maxima')

    vol_ids = fields.One2many('plane.vol', 'avio_id', string='Vols')

    def _get_name(self):
        for record in self:
            record.name = str(record.marca + ' ' + record.model)