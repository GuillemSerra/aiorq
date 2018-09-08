import asyncio

import pytest

from aiorq.backends import get_conn, init_redis
from aiorq.jobs import Job
from aiorq.jobs.repos import enqueue_job


pytestmark = pytest.mark.asyncio


@pytest.fixture
async def redis(event_loop):
    await init_redis(event_loop)
    redis = get_conn()
    yield redis

    await redis.flushall()


async def test_enqueue_job(redis):
    job = Job(id='fake_id', task=asyncio.sleep(1))

    await enqueue_job(job)

    assert bool(redis.exists(job.id)) is True
    assert await redis.llen(job.queue) != 0
