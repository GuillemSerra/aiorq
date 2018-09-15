import pickle

from aioredis import Redis

from backends import redis_conn
from jobs import Job


@redis_conn
async def enqueue_job(redis: Redis, job: Job):
    await redis.set(job.id, pickle.dumps(job))
    await redis.lpush(job.queue_id, job.id)


@redis_conn
async def get_job(redis: Redis, queue_id: str) -> Job:
    _queue, job_id = await redis.brpop(queue_id)
    job = await redis.get(job_id)
    job_entity = pickle.loads(job)

    return job_entity
