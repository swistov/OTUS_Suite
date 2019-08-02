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
    from smtplib import SMTP_SSL
    from email.mime.text import MIMEText

    # Данные для подключения
    fromaddr = 'swip88@bk.ru'
    password = 'rfnvfylE1988'

    # формирование сообщения
    msg = MIMEText('Some', "", "utf-8")
    msg['From'] = fromaddr
    msg['To'] = 'nsvistov@gridgain.com'
    msg['Subject'] = "Ошибка в скрипте MNP"

    # отправка
    smtp = SMTP_SSL('smtp.mail.ru:465')
    smtp.ehlo()
    smtp.login(fromaddr, password)
    smtp.sendmail(fromaddr, 'nsvistov@gridgain.com', msg.as_string())
    smtp.quit()
    return f'Mail send {job}'
