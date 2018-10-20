import uuid
from datetime import datetime

from dataclasses import dataclass
from jobs import Job
from jobs.repos import JobRepo


@dataclass
class EnqueueJobUseCase:
    job: Job
    _job_repo: JobRepo = JobRepo()

    async def execute(self) -> Job:
        self.job.id = str(uuid.uuid4())
        self.job.queued_time = datetime.now()
        await self._job_repo.enqueue(self.job)

        return self.job


@dataclass
class GetJobUseCase:
    queue_id: str
    _job_repo: JobRepo = JobRepo()

    async def execute(self) -> Job:
        return await self._job_repo.get(self.queue_id)


@dataclass
class ExecuteJobUseCase:
    job: Job

    async def execute(self):
        return await self.job.task()
