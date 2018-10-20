import asyncio

import pytest

from jobs import Job
from jobs.repos import JobRepo


pytestmark = pytest.mark.asyncio


async def test_enqueue_job(redis):
    job_repo = JobRepo(_redis=redis)
    job = Job(id='fake_id',
              task=asyncio.sleep,
              queue_id='test_queue')

    await job_repo.enqueue(job)

    assert bool(redis.exists(job.id)) is True
    assert await redis.llen(job.queue_id) != 0


async def test_get_job(redis):
    job_repo = JobRepo(_redis=redis)
    expected_job = Job(id='fake_id',
                       task=asyncio.sleep,
                       queue_id='test_queue')

    await job_repo.enqueue(expected_job)
    result_job = await job_repo.get(expected_job.queue_id)

    assert isinstance(result_job, Job)
    assert result_job == expected_job
