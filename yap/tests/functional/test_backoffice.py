from yap.tests import *

class TestBackofficeController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='backoffice'))
        # Test response...
