
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.modules.company.tests import CompanyTestMixin
from trytond.tests.test_tryton import ModuleTestCase


class AccountDunningRelatedInvoiceTestCase(CompanyTestMixin, ModuleTestCase):
    'Test AccountDunningRelatedInvoice module'
    module = 'account_dunning_related_invoice'


del ModuleTestCase
