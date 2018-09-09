import pytest

from aiorq.consumer import consume_queue
from jobs import Job, enqueue_job_use_case
from queues import Queue

pytestmark = pytest.mark.asyncio


async def test_consumer_integration(redis):
    var_to_change = 0

    async def task_to_change_var():
        global var_to_change
        var_to_change = 1

    queue = Queue(id='test_queue')
    job = Job(queue_id=queue.id, task=task_to_change_var)
    await enqueue_job_use_case(job)

    await consume_queue(queue)

    assert var_to_change == 1
