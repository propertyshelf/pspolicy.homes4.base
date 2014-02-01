# -*- coding: utf-8 -*-
"""Test settings applied by pspolicy.homes4.base."""

# python imports
import unittest2 as unittest

# zope imports
from Products.CMFCore.utils import getToolByName
from plone.app.caching.interfaces import IPloneCacheSettings
from plone.cachepurging.interfaces import ICachePurgingSettings
from plone.caching.interfaces import ICacheSettings
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

# local imports
from pspolicy.homes4.base.testing import (
    PSPOLICY_HOMES4_BASE_INTEGRATION_TESTING,
)


class TestSettings(unittest.TestCase):
    """Settings Test Case for pspolicy.homes4.base."""
    layer = PSPOLICY_HOMES4_BASE_INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer['portal']
        self.p_properties = getToolByName(self.portal, 'portal_properties')
        self.portal_workflow = getToolByName(self.portal, 'portal_workflow')
        self.registry = getUtility(IRegistry)

    def test_cache_settings(self):
        """Validate the plone.app.caching settings."""
        settings = self.registry.forInterface(ICacheSettings)
        self.assertTrue(settings.enabled)

    def test_dc_metadata_exposed(self):
        """Validate the DC Core metadata option is enabled."""
        sp = self.p_properties.get('site_properties')
        self.failUnless(sp)
        self.assertTrue(getattr(sp, "exposeDCMetaTags"))

    def test_mailhost_host(self):
        """Validate the SMTP Server settings."""
        mailhost = getToolByName(self.portal, 'MailHost')
        self.assertEquals('localhost', mailhost.smtp_host)
        self.assertEquals(25, mailhost.smtp_port)

    def test_plone_cache_settings(self):
        """Validate the plone.app.caching settings."""
        settings = self.registry.forInterface(IPloneCacheSettings)
        self.assertTrue(settings.enableCompression)
        mapping = settings.templateRulesetMapping
        self.assertIn('leadImage', mapping.keys())
        self.assertIn('leadImage_preview', mapping.keys())
        self.assertIn('leadImage_thumb', mapping.keys())
        self.assertEquals('plone.content.file', mapping.get('leadImage'))
        self.assertEquals(
            'plone.content.file',
            mapping.get('leadImage_preview'),
        )
        self.assertEquals(
            'plone.content.file',
            mapping.get('leadImage_thumb'),
        )

    def test_plone_cache_purge_settings(self):
        """Validate the plone.cachepurging settings."""
        settings = self.registry.forInterface(ICachePurgingSettings)
        self.assertTrue(settings.enabled)
        self.assertTrue(settings.virtualHosting)
        self.assertEquals(('http://localhost:9000',), settings.cachingProxies)

    def test_site_title(self):
        """Validate the site title."""
        self.assertEquals("Homes4", self.portal.getProperty("title"))

    def test_sitemap_enabled(self):
        """Validate that sitemap.xml.gz option is enabled."""
        sp = self.p_properties.get('site_properties')
        self.failUnless(sp)
        self.assertTrue(getattr(sp, "enable_sitemap"))

    def test_tinymce_settings(self):
        """Validate TinyMCE editor settings."""
        utility = getToolByName(self.portal, 'portal_tinymce')
        self.assertTrue(utility.link_using_uids)
        self.assertTrue(utility.toolbar_visualchars)
        self.assertTrue(utility.toolbar_media)
        self.assertTrue(utility.toolbar_removeformat)
        self.assertTrue(utility.toolbar_pasteword)
        self.assertTrue(utility.toolbar_pastetext)
        self.assertTrue(utility.toolbar_visualaid)
        self.assertTrue(utility.toolbar_cleanup)
