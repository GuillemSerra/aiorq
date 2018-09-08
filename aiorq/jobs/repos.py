import pickle

from aioredis import Redis

from aiorq.backends import redis_conn
from .entities import Job


@redis_conn
async def enqueue_job(redis: Redis, job: Job) -> Job:
    await redis.set(Job.id, pickle.dumps(Job))
    await redis.lpush(Job.queue, Job.id)

    return Job
