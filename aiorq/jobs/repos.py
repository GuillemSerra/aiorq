import pickle

from aioredis import Redis

from backends import redis_conn
from jobs import Job


@redis_conn
async def enqueue_job(redis: Redis, job: Job):
    await redis.set(job.id, pickle.dumps(job))
    await redis.lpush(job.queue, job.id)
