import requests
from django.contrib.auth.models import User

from django_rq import job
from email.mime.text import MIMEText
from main.models import CurrencyRate, Lesson
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


def send_email(email, subject, content):
    fromaddr = 'example@mail.ru'
    password = 'MySuperPassword'

    # Configuration message
    msg = MIMEText(content, 'html')
    msg['From'] = fromaddr
    msg['To'] = email
    msg['Subject'] = subject

    # Send e-mail
    smtp = SMTP_SSL('smtp.mail.ru:465')
    smtp.ehlo()
    smtp.login(fromaddr, password)
    smtp.sendmail(fromaddr, email, msg.as_string())
    smtp.quit()
    return True


@job('high')
def send_simple_message(username):
    user = User.objects.get(username=username)
    # domain = str(get_current_site(request)),
    token = user.auth_token.key
    domain = 'http://127.0.0.1:8000/'
    subject = '[OTUS] Валидация e-mail'

    content = f''' Hi {username}.
                Click to url for end registration.
                <a href="{domain}user/verify/?user={username}&token={token}"><h4>VALIDATION</h4></a>'''

    if send_email(user.email, subject, content):
        return f'Mail send user {username}, email: {user.email}. JOB: {job}.'
    else:
        return f'Message not send. Username: {username}'


@job('high')
def send_reminder_letter(email, lesson_id):
    try:
        lesson = Lesson.objects.get(pk=lesson_id)
        user = User.objects.get(email=email)
    except:
        print('Error')

    subject = '[OTUS] Скоро начнётся урок'

    content = f'''
                Привет, {user.username}.
                Продолжаем урок {lesson.curse.name}.
                В {lesson.date_time_release.time()} начнётся урок {lesson.name}.
                '''
    if send_email(user.email, subject, content):
        return f'Mail send user {user.username}, email: {user.email}. JOB: {job}.'

    return f'Message not send. Username: {user.username}'
