import uuid
from datetime import datetime

from jobs.repos import enqueue_job
from jobs.entities import Job


async def enqueue_job_use_case(job: Job):
    job.id = str(uuid.uuid4())
    job.queued_time = datetime.now()
    return await enqueue_job(job)
