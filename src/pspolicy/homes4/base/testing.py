from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import pspolicy.homes4.base


PSPOLICY_HOMES4_BASE = PloneWithPackageLayer(
    zcml_package=pspolicy.homes4.base,
    zcml_filename='testing.zcml',
    gs_profile_id='pspolicy.homes4.base:testing',
    name="PSPOLICY_HOMES4_BASE")

PSPOLICY_HOMES4_BASE_INTEGRATION = IntegrationTesting(
    bases=(PSPOLICY_HOMES4_BASE, ),
    name="PSPOLICY_HOMES4_BASE_INTEGRATION")

PSPOLICY_HOMES4_BASE_FUNCTIONAL = FunctionalTesting(
    bases=(PSPOLICY_HOMES4_BASE, ),
    name="PSPOLICY_HOMES4_BASE_FUNCTIONAL")
