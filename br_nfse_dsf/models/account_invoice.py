# -*- coding: utf-8 -*-
# © 2016 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

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

    def _return_pdf_invoice(self, doc):
        if doc.model == '016':  # Provedor DSF
            return 'br_nfse_dsf.report_br_nfse_danfe'
        return super(AccountInvoice, self)._return_pdf_invoice(doc)

    def _prepare_edoc_item_vals(self, line):
        res = super(AccountInvoice, self)._prepare_edoc_item_vals(line)
        res['codigo_servico_dsf'] = \
            line.service_type_id.codigo_servico_dsf
        return res

    def _prepare_edoc_vals(self, invoice, inv_lines, serie_id):
        res = super(AccountInvoice, self)._prepare_edoc_vals(
            invoice, inv_lines, serie_id)
        res['operation'] = self.operation
        res['tributacao'] = self.tributacao
        res['tipo_recolhimento'] = self.tipo_recolhimento
        return res

    @api.onchange('fiscal_position_id')
    def _onchange_br_account_fiscal_position_id(self):
        res = super(AccountInvoice, self)\
            ._onchange_br_account_fiscal_position_id()
        if self.fiscal_position_id:
            fiscal_id = self.fiscal_position_id
            if fiscal_id.tributacao:
                self.tributacao = fiscal_id.tributacao
            if fiscal_id.operation:
                self.operation = fiscal_id.operation
            if fiscal_id.tipo_recolhimento:
                self.tipo_recolhimento = fiscal_id.tipo_recolhimento
        return res
