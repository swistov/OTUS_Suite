from main.tasks import send_simple_message
from redis import Redis
from django_rq import job


redis_conn = Redis(host='195.201.131.110',
                   port=6379,
                   password='a5ff74c136c8e7b58f0850dfe19b15b70b75e8e22892da4d261131f7327dcd81')


@job('high', connection=redis_conn)
def send_validation_message(username):
    send_job = send_simple_message.delay(username)
    return send_job

# schedule = django_rq.get_scheduler('default')
# schedule.get_jobs()
#
# for job in schedule.get_jobs():
#     print(job.description)
#
# for job in schedule.get_jobs():
#     schedule.cancel(job)
#
#
#
# python manage.py rqworker default high
# python manage.py rqscheduler
