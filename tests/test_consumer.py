import pytest

from aiorq.consumer import consume_queue
from jobs import Job, enqueue_job_use_case
from queues import Queue


pytestmark = pytest.mark.asyncio


async def task():
    return 1


async def test_consumer_integration(redis):
    queue = Queue(id='test_queue')
    job = Job(queue_id=queue.id, task=task)
    await enqueue_job_use_case(job)

    result = await consume_queue(queue)

    assert result == 1
