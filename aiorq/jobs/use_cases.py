import uuid
from datetime import datetime

from jobs import repos, Job


async def enqueue_job_use_case(job: Job) -> Job:
    job.id = str(uuid.uuid4())
    job.queued_time = datetime.now()

    await repos.enqueue_job(job)

    return Job
