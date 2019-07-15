import requests
from django_rq import job
from main.models import CurrencyRate


@job('default')
def update_currency_rate():
    queryset = CurrencyRate.objects.all()

    for rate in queryset:
        pair = '{}RUB'.format(rate.currency.upper())
        response = requests.get(
            'https://www.freeforexapi.com/api/live?pairs={}'.format(pair)
        )

        data = response.json()
        rate.rate = data['rates'][pair]['rate']
        rate.save(update_fields=['rate'])

    return True


@job('high')
def send_email(email_text, user_id):
    pass
