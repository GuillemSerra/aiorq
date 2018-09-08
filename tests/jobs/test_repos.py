import asyncio

import pytest

from backends import get_conn, init_redis, stop_redis
from jobs import Job
from jobs.repos import enqueue_job


pytestmark = pytest.mark.asyncio


@pytest.fixture
async def redis(event_loop):
    await init_redis(event_loop)
    redis = get_conn()
    yield redis

    await redis.flushall()
    await stop_redis()


async def test_enqueue_job(redis):
    job = Job(id='fake_id', task=asyncio.sleep)

    await enqueue_job(job)

    assert bool(redis.exists(job.id)) is True
    assert await redis.llen(job.queue) != 0
