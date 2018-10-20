import pytest

from consumer import ConsumeQueue
from jobs import Job, EnqueueJobUseCase
from queues import Queue


pytestmark = pytest.mark.asyncio


async def test_consumer_integration(redis):
    async def task():
        return 1

    queue = Queue(id='test_queue')
    job = Job(queue_id=queue.id, task=task)
    await EnqueueJobUseCase(job).execute()

    result = await ConsumeQueue(queue).execute()

    assert result == 1
