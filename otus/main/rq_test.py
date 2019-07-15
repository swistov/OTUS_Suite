import requests
from redis import Redis
from rq import Queue
from rq.decorators import job
from rq_scheduler import Scheduler
from  datetime import datetime, timedelta


redis_conn = Redis(host='192.168.12.156', port=6379)


@job('default', connection=redis_conn)
def get_currency_rate(currency):
    pair = '{}RUB'.format(currency)
    response = requests.get(
        'https://www.freeforexapi.com/api/live?pairs={}'.format(pair)
    )

    data = response.json()
    return data['rates'][pair]['rate']


scheduler = Scheduler(connection=redis_conn)
scheduler.enqueue_at(datetime(2019, 7, 15, 9,0), get_currency_rate, 'USD')
