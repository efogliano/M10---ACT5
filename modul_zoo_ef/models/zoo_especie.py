from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    name = fields.Char(compute='_get_name', string="Noms", readonly="true", store=False)
    perill = fields.Char('Perill')
    nomVulgar = fields.Char('Nom Vulgar')
    nomCientific = fields.Char('Nom cientific')
    familia = fields.Char('Familia')

    animal_ids = fields.One2many('zoo.animal', 'especie_id', string='Animals')

    def _get_name(self):
        for record in self:
            record.name = str(record.nomCientific) + ' ' + str(record.nomVulgar)