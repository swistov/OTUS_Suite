import django_rq
import requests
from redis.client import Redis
from rq import Queue
from rq.decorators import job
from rq_scheduler import Scheduler
from datetime import datetime, timedelta

from django.conf import settings

redis_conn = Redis(host=settings.REDIS_HOST,
                   port=settings.REDIS_PORT,
                   password=settings.REDIS_PASSWORD)


@job('default', connection=redis_conn)
def get_currency_rate(currency):
    pair = '{}RUB'.format(currency)
    try:
        response = requests.get(
            'https://www.freeforexapi.com/api/live?pairs={}'.format(pair)
        )
    except ConnectionError as e:
        return 'Bad request. Error: {}'.format(e)

    data = response.json()
    return data['rates'][pair]['rate']

# TODO:
# scheduler = Scheduler(connection=redis_conn)
# scheduler.enqueue_at(datetime(2019, 7, 15, 9, 0), get_currency_rate, 'USD')
