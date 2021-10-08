# This file is part account_dunning_related_invoice module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import account

def register():
    Pool.register(
        account.Dunning,
        module='account_dunning_related_invoice', type_='model')
