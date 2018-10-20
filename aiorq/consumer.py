from dataclasses import dataclass
from jobs import ExecuteJobUseCase, GetJobUseCase
from queues import Queue


@dataclass
class ConsumeQueue:
    queue: Queue
    _get_job_use_case: GetJobUseCase = GetJobUseCase
    _execute_job_use_case: ExecuteJobUseCase = ExecuteJobUseCase

    async def consume(self):
        job = await self._get_job_use_case(self.queue.id).execute()
        return await self._execute_job_use_case(job).execute()
