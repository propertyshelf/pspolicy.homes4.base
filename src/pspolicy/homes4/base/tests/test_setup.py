# -*- coding: utf-8 -*-
"""Test Setup of pspolicy.homes4.base."""

# python imports
import unittest2 as unittest

# local imports
from pspolicy.homes4.base.testing import (
    PSPOLICY_HOMES4_BASE_INTEGRATION_TESTING,
)


class TestSetup(unittest.TestCase):
    """Setup Test Case for pspolicy.homes4.base."""

    layer = PSPOLICY_HOMES4_BASE_INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.app = self.layer['app']
        self.portal = self.layer['portal']

    def test_product_is_installed(self):
        """Validate that our product is installed."""
        qi = self.portal.portal_quickinstaller
        self.assertTrue(qi.isProductInstalled('pspolicy.homes4.base'))

    def test_products_ploneformgen_installed(self):
        """Test that Products.PloneFormGen is installed."""
        qi = self.portal.portal_quickinstaller
        self.assertTrue(qi.isProductInstalled('PloneFormGen'))

    def test_collective_contentleadimage_installed(self):
        """Test that collective.contentleadimage is installed."""
        qi = self.portal.portal_quickinstaller
        self.assertTrue(qi.isProductInstalled('collective.contentleadimage'))

    def test_plone_app_caching_installed(self):
        """Test that plone.app.caching is installed."""
        qi = self.portal.portal_quickinstaller
        if qi.isProductAvailable('plone.app.caching'):
            self.assertTrue(qi.isProductInstalled('plone.app.caching'))
        else:
            self.assertTrue(
                'plone.app.caching' in qi.listInstallableProfiles())

    def test_plone_app_theming_installed(self):
        """Test that plone.app.theming is installed."""
        qi = self.portal.portal_quickinstaller
        if qi.isProductAvailable('plone.app.theming'):
            self.assertTrue(qi.isProductInstalled('plone.app.theming'))
        else:
            self.assertTrue(
                'plone.app.theming' in qi.listInstallableProfiles())

    def test_plone_mls_listing_installed(self):
        """Test that plone.mls.listing is installed."""
        qi = self.portal.portal_quickinstaller
        self.assertTrue(qi.isProductInstalled('plone.mls.listing'))
