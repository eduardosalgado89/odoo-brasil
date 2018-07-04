# group name="nfe"

from odoo import models, fields


class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'

    operation = fields.Selection(
        [('A', 'Sem dedução'),
         ('B', 'Com dedução/Materiais'),
         ('C', 'Imune/Isenta ISSQN'),
         ('D', 'Devolução/Simples Remessa'),
         ('J', 'Intermediação')], u"Operação",
        default='A')

    tributacao = fields.Selection(
        [('C', 'Isenta de ISS'),
         ('E', 'Não Incidência no Município'),
         ('F', 'Imune'),
         ('K', 'Exigilidade Susp. Dec J/Proc. A'),
         ('N', 'Não Tributável'),
         ('T', 'Tributável'),
         ('G', 'Tributável Fixo'),
         ('H', 'Tributável S.N.'),
         ('M', 'Micro Empreendedor Individual (MEI)')],
        u"Tributação", default='T')

    tipo_recolhimento = fields.Selection(
        [('A', 'A Recolher'),
         ('R', 'Retido na fonte')],
        u"Tipo de Recolhimento", default="A")
