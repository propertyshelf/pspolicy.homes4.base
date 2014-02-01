# -*- coding: utf-8 -*-
"""Test settings applied by pspolicy.homes4.base."""

# python imports
import unittest2 as unittest

# zope imports
from Products.CMFCore.utils import getToolByName

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

    def test_mailhost_host(self):
        """Test that the correct SMTP Server is set."""
        mailhost = getToolByName(self.portal, 'MailHost')
        self.assertEquals('localhost', mailhost.smtp_host)
        self.assertEquals(25, mailhost.smtp_port)
