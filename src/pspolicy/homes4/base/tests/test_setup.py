# -*- coding: utf-8 -*-
import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from pspolicy.homes4.base.testing import\
    PSPOLICY_HOMES4_BASE_INTEGRATION


class TestExample(unittest.TestCase):

    layer = PSPOLICY_HOMES4_BASE_INTEGRATION

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_is_installed(self):
        """Validate that our product is installed."""
        pid = 'pspolicy.homes4.base'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(
            pid in installed,
            'package appears not to have been installed',
        )
