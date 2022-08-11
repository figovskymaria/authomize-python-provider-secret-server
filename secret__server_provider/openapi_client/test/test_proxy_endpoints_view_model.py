"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import plugins
from plugins.model.proxy_engine_view_model import ProxyEngineViewModel
from plugins.model.proxy_node_view_model import ProxyNodeViewModel
from plugins.model.proxy_site_view_model import ProxySiteViewModel
globals()['ProxyEngineViewModel'] = ProxyEngineViewModel
globals()['ProxyNodeViewModel'] = ProxyNodeViewModel
globals()['ProxySiteViewModel'] = ProxySiteViewModel
from plugins.model.proxy_endpoints_view_model import ProxyEndpointsViewModel


class TestProxyEndpointsViewModel(unittest.TestCase):
    """ProxyEndpointsViewModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProxyEndpointsViewModel(self):
        """Test ProxyEndpointsViewModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProxyEndpointsViewModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
