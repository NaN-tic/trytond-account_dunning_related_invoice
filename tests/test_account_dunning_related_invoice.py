# This file is part account_dunning_related_invoice module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class AccountDunningRelatedInvoiceTestCase(ModuleTestCase):
    'Test Account Dunning Related Invoice module'
    module = 'account_dunning_related_invoice'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            AccountDunningRelatedInvoiceTestCase))
    return suite
