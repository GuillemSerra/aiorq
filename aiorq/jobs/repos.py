import pickle

from aioredis import Redis

from backends import get_conn
from dataclasses import dataclass
from jobs import Job


@dataclass
class JobRepo:
    _redis: Redis = get_conn()

    async def enqueue(self, job: Job):
        await self._redis.set(job.id, pickle.dumps(job))
        await self._redis.lpush(job.queue_id, job.id)

    async def get(self, queue_id: str) -> Job:
        _queue, job_id = await self._redis.brpop(queue_id)
        job = await self._redis.get(job_id)
        return pickle.loads(job)
