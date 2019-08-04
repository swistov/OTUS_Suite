# import os
# import django
# os.environ['DJANGO_SETTINGS_MODULE'] = 'otus.settings'
# django.setup()


import requests
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site

from django_rq import job
from email.mime.text import MIMEText
from main.models import CurrencyRate
from smtplib import SMTP_SSL


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
def send_simple_message(username):
    user = User.objects.get(username=username)
    # domain = str(get_current_site(request)),
    token = user.auth_token.key
    domain = 'http://127.0.0.1:8000/'
    fromaddr = 'example@example.com'
    password = 'MySuperPassword'

    content = f''' Hi {username}.
                Click to url for end registration.
                <a href="{domain}user/verify/?user={username}&token={token}"><h4>VALIDATION</h4></a>'''

    # Configuration message
    msg = MIMEText(content, 'html')
    msg['From'] = fromaddr
    msg['To'] = user.email
    msg['Subject'] = '[OTUS] Валидация e-mail'

    # Send e-mail
    smtp = SMTP_SSL('smtp.mail.ru:465')
    smtp.ehlo()
    smtp.login(fromaddr, password)
    smtp.sendmail(fromaddr, user.email, msg.as_string())
    smtp.quit()
    return f'Mail send user {username}, email: {user.email}. JOB: {job}.'
