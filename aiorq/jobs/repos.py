import pickle

from aioredis import Redis

from aiorq.backends import redis_conn
from .entities import Job


@redis_conn
async def enqueue_job(redis: Redis, job: Job):
    await redis.set(job.id, pickle.dumps(job))
    await redis.lpush(job.queue, job.id)
