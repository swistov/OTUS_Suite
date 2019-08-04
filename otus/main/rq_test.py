import django_rq
import requests
from redis import Redis
from rq import Queue
from rq.decorators import job
from rq_scheduler import Scheduler
from datetime import datetime, timedelta


redis_conn = Redis(host='195.201.131.110',
                   port=6379,
                   password='a5ff74c136c8e7b58f0850dfe19b15b70b75e8e22892da4d261131f7327dcd81')


@job('default', connection=redis_conn)
def get_currency_rate(currency):
    pair = '{}RUB'.format(currency)
    response = requests.get(
        'https://www.freeforexapi.com/api/live?pairs={}'.format(pair)
    )

    data = response.json()
    return data['rates'][pair]['rate']


# scheduler = Scheduler(connection=redis_conn)
# scheduler.enqueue_at(datetime(2019, 7, 15, 9, 0), get_currency_rate, 'USD')
