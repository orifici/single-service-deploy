import unittest
from unittest import mock
from miner import DataMiner


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        """ Helper class. Mocks a request.get response.json """

        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    return MockResponse({"bpi": {"USD": {"rate_float": 10}}})


class TestDataMiner(unittest.TestCase):
    """ Test cases for the DataMiner class """

    @mock.patch('miner.requests.get', side_effect=mocked_requests_get)
    def test_call_api(self, mocked_response):
        """ Test a mocked call to the api """

        api_handler = DataMiner(endpoint="dummy", currency='USD')
        api_handler.call_api()
        self.assertEqual(api_handler.prices[0], 10.0)
