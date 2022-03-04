from factory.main_factory import create_app
from asynctest import TestCase

class BaseSetup(TestCase):
    def setUp(self):
        app = create_app()
        app.config.update({
            "TESTING": True,
        })

        self.app = app
        self.client = app.test_client()
