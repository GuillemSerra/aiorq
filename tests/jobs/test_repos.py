import asyncio

import pytest

from jobs import Job
from jobs.repos import enqueue_job, get_job


pytestmark = pytest.mark.asyncio


async def test_enqueue_job(redis):
    job = Job(id='fake_id',
              task=asyncio.sleep,
              queue_id='test_queue')

    await enqueue_job(job)

    assert bool(redis.exists(job.id)) is True
    assert await redis.llen(job.queue_id) != 0


async def test_get_job(redis):
    expected_job = Job(id='fake_id',
                       task=asyncio.sleep,
                       queue_id='test_queue')

    await enqueue_job(expected_job)
    result_job = await get_job(expected_job.queue_id)

    assert isinstance(result_job, Job)
    assert result_job == expected_job
