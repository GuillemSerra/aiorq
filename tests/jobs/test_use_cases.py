import pytest
from jobs import Job, EnqueueJobUseCase, ExecuteJobUseCase
from unittest.mock import MagicMock


pytestmark = pytest.mark.asyncio


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)


async def test_enqueue_job_successfully():
    job = Job(id='fake_id')
    repo_mock = AsyncMock()
    use_case = EnqueueJobUseCase(job, _job_repo=repo_mock)

    await use_case.execute()

    assert job.id != 'fake_id'
    assert job.queued_time is not None
    repo_mock.enqueue.assert_called_once()


async def test_execute_job_use_case():
    async def task():
        return 1

    job = Job(task=task)
    use_case = ExecuteJobUseCase(job)

    result = await use_case.execute()

    assert result == 1
