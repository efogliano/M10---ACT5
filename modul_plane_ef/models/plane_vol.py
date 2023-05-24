from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    passatgers = fields.Integer('Passatgers')
    dataSortida = fields.Date('Data Sortida')
    dataArrivada = fields.Date('Data Arrivada')

    avio_id = fields.Many2one('plane.avio', string='Avio')
    pilot_id = fields.Many2one('plane.pilot', string='Pilot')
    desti_id = fields.Many2one('plane.aeroport', string='Aeroport desti')
    origen_id = fields.Many2one('plane.aeroport', string='Aeroport origen')