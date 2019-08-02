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


@job('high', connection=redis_conn)
def send_simple_message():
    from smtplib import SMTP_SSL
    from email.mime.text import MIMEText

    # Данные для подключения
    fromaddr = 'lol@mail.ru'
    password = 'SuperP@$$w0rd'

    # формирование сообщения
    msg = MIMEText('Some', '123', "utf-8")
    msg['From'] = fromaddr
    msg['To'] = 'i.mail.ru'
    msg['Subject'] = "Почта"

    # отправка
    smtp = SMTP_SSL('smtp.mail.ru:465')
    smtp.ehlo()
    smtp.login(fromaddr, password)
    smtp.sendmail(fromaddr, 'i.mail.ru', msg.as_string())
    smtp.quit()
    return True


schedule = django_rq.get_scheduler('default')
schedule.get_jobs()

for job in schedule.get_jobs():
    print(job.description)

for job in schedule.get_jobs():
    schedule.cancel(job)

python manage.py rqworker default high
python manage.py rqscheduler
