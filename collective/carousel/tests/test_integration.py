"""This is an integration test. It uses PloneTestCase, but does not
use doctest syntax.

You will find lots of examples of this type of test in CMFPlone/tests, for 
example.
"""

import unittest
from collective.carousel.tests.base import CarouselTestCase

from Products.CMFCore.utils import getToolByName

class TestCarousel(CarouselTestCase):
    """The name of the class should be meaningful. This may be a class that
    tests the installation of a particular product.
    """

    def test_js_available(self):
        pass
        
    def test_css_available(self):
        pass        

    def test_view_available_for_collection(self):
        pass
        
    def test_view_is_selectable(self):
        pass
        
    # Keep adding methods here, or break it into multiple classes or
    # multiple files as appropriate. Having tests in multiple files makes
    # it possible to run tests from just one package:
    #
    #   ./bin/instance test -s example.tests -t test_integration_unit


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCarousel))
    return suite