from datetime import datetime, timedelta

from django.utils import timezone

from main.models import Lesson
from main.tasks import send_simple_message, send_reminder_letter
from redis import Redis
from django_rq import job


redis_conn = Redis(host='195.201.131.110',
                   port=6379,
                   password='a5ff74c136c8e7b58f0850dfe19b15b70b75e8e22892da4d261131f7327dcd81')


@job('high', connection=redis_conn)
def send_validation_message(username):
    send_job = send_simple_message.delay(username)
    return send_job


@job('default', connection=redis_conn)
def reminder_letter():
    for lesson in Lesson.objects.all().filter(enabled=True):
        delta = datetime.now(timezone.utc)-lesson.date_time_release
        if delta.seconds < 3600 and lesson.curse.enabled:
            for student in lesson.curse.students.prefetch_related():
                send_reminder_letter.delay(student.user.email, lesson.id)
                return f'Message send to {student}'
        return f'Not lessons'


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
