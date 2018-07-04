from odoo import fields, models


class ResStateCity(models.Model):
    _inherit = 'res.state.city'

    siafi_code = fields.Char(
        u'Código SIAFI', size=10)
