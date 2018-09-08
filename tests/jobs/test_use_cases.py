import pytest
from aiorq.jobs import Job, enqueue_job_use_case
from unittest.mock import MagicMock, patch


pytestmark = pytest.mark.asyncio


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class TestEnqueueJobUseCase:

    @patch('jobs.use_cases.repos', new_callable=AsyncMock)
    async def test_enqueue_job_successfully(self, repo_mock):
        job = Job(id='fake_id')

        await enqueue_job_use_case(job)
        
        assert job.id != 'fake_id'
        assert job.queued_time is not None
        assert repo_mock.enqueue_job.assert_called_once()
