from unittest import mock
from django.test import TestCase

from main.models import CurrencyRate
from main.tasks import get_currency_rate, update_currency_rates


class FakeResponse:
    def json(self):
        return {
            "rates": {
                "USDRUB": {
                    "rate": 63.0,
                    "timestamp": 1572718986
                }
            },
            "code": 200
        }


class CurrencyRateTestCase(TestCase):

    @mock.patch('requests.get', return_value=FakeResponse())
    def test_get_currency_rate(self, mocked_get):
            rate = get_currency_rate('usd')
            self.assertEqual(rate, 63.0)

    @mock.patch('requests.get', return_value=FakeResponse())
    def test_update_currency_rates(self, mocked_get):
        rate = CurrencyRate.objects.create(currency='usd')
        self.assertEqual(rate.rate, 1)

        self.assertTrue(update_currency_rates())
        rate = CurrencyRate.objects.get(currency='usd')
        self.assertEqual(rate, 63.000000)
