from datetime import datetime, timedelta

from django.utils import timezone
from django.conf import settings
from main.models import Lesson
from main.tasks import send_simple_message, send_reminder_letter
from redis import Redis
from django_rq import job

redis_conn = Redis(host=settings.REDIS_HOST,
                   port=settings.REDIS_PORT,
                   password=settings.REDIS_PASSWORD)


@job('high', connection=redis_conn)
def send_validation_message(username):
    send_job = send_simple_message.delay(username)
    return send_job


@job('default', connection=redis_conn)
def reminder_letter():
    time_delta = datetime.now(timezone.utc) - timedelta(hours=1)
    for lesson in Lesson.objects.all().filter(enabled=True,
                                              date_time_release__range=(time_delta, datetime.now(timezone.utc))):

        for student in lesson.curse.students.prefetch_related():
            send_reminder_letter.delay(student.user.email, lesson.id)
            return f'Message send to {student}'
    return f'Not lessons'


# TODO
# Command for start worker

# schedule = django_rq.get_scheduler('default')
# schedule.get_jobs()

# Delete jobs
# for job in schedule.get_jobs():
#     schedule.cancel(job)

# python manage.py rqworker default high
# python manage.py rqscheduler

# Start scheduler
# scheduler = django_rq.get_scheduler('high')
# scheduler.enqueue_in(timedelta(seconds=5), reminder_letter.delay())
