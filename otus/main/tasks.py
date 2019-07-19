import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'otus.settings'
django.setup()


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
def send_simple_message():
    send = requests.post(
        "https://api.mailgun.net/v3/sandbox1432a76c6cbe403db25aa89a09eb0fa3.mailgun.org/messages",
        auth=("api", "722a8cb7b417f3030fdf1779a6122ca3-fd0269a6-a05c6376"),
        data={"from": "Excited User <mailgun@sandbox1432a76c6cbe403db25aa89a09eb0fa3.mailgun.org>",
              "to": ['swip88@bk.ru', "swistov@sandbox1432a76c6cbe403db25aa89a09eb0fa3.mailgun.org"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
    return send
