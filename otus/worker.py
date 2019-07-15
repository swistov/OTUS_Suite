from django.conf import settings
from redis import Redis
from rq import Worker, Queue, Connection


listen = ['high', 'default', 'low']
conn = Redis(host='195.201.131.110',
             port=6379,
             password='a5ff74c136c8e7b58f0850dfe19b15b70b75e8e22892da4d261131f7327dcd81')

settings.configure()

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
