import django
from django.test.client import RequestFactory
from django.test import SimpleTestCase
from django.conf import settings
from raygun4py.middleware.django import Provider

settings.configure(DEBUG=True)
django.setup()

class DjangoProviderTests(SimpleTestCase):

    def setUp(self):
        request_factory = RequestFactory()
        self.get_request = request_factory.get('/foo')

    def test_map_request(self):
        request_payload = Provider._mapRequest(None, self.get_request)
        self.assertEqual(request_payload['url'], '/foo')
        self.assertEqual(request_payload['httpMethod'], 'GET')

    def test_get_django_environment(self):
        environment_payload = Provider._get_django_environment(self)
        self.assertEqual(environment_payload['frameworkVersion'], django.get_version())