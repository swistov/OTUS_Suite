import requests
from redis import Redis
from rq import Queue


queue = Queue(connection=Redis('192.168.12.156', 6379))


def get_currency_rate(currency):
    pair = '{}RUB'.format(currency)
    response = requests.get(
        'https://www.freeforexapi.com/api/live?pairs={}'.format(pair)
    )

    data = response.json()
    return data['rates'][pair]['rate']

