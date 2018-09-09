from jobs import execute_job_use_case, get_job_use_case
from queues import Queue


async def consume_queue(queue: Queue):
    job = await get_job_use_case(queue.id)
    await execute_job_use_case(job)
