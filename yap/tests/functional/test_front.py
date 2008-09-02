from yap.tests import *

class TestFrontController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='front'))
        # Test response...
