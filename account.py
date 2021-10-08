# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.model import fields


class Dunning(metaclass=PoolMeta):
    __name__ = 'account.dunning'

    invoice = fields.Function(fields.Many2One('account.invoice', "Invoice"),
        'get_invoice')

    @classmethod
    def get_invoice(cls, dunnings, name):
        pool = Pool()
        Invoice = pool.get('account.invoice')

        res = dict((d.id, None) for d in dunnings)
        for dunning in dunnings:
            if dunning.line and dunning.line.move_origin and isinstance(dunning.line.move_origin, Invoice):
                res[dunning.id] = dunning.line.move_origin.id
        return res