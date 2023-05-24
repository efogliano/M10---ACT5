from odoo import models, fields
class plane_pilot(models.Model):
    _name = 'plane.pilot'
    name = fields.Char(compute='_get_name', string="Nom complet", readonly="true", store=False)
    nom = fields.Char('Nom')
    cognoms = fields.Char('Cognom')
    nif = fields.Char('NIF')
    telf = fields.Char('Numero de telefon')
    email = fields.Char('Correu electronic')

    vol_ids = fields.One2many('plane.vol', 'pilot_id', string='Vols')

    def _get_name(self):
        for record in self:
            record.name = str(record.nom) + ' ' + str(record.cognoms)