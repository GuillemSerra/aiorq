import pytest
from jobs import Job, enqueue_job_use_case, execute_job_use_case
from unittest.mock import MagicMock, patch


pytestmark = pytest.mark.asyncio


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)


@pytest.mark.skip(reason='wtf')
class TestEnqueueJobUseCase:

    @patch('jobs.use_cases.repos', new_callable=AsyncMock)
    async def test_enqueue_job_successfully(self, repo_mock):
        job = Job(id='fake_id')

        await enqueue_job_use_case(job)

        assert job.id != 'fake_id'
        assert job.queued_time is not None
        assert repo_mock.enqueue_job.assert_called_once()


async def test_execute_job_use_case():
    variable_to_change_when_task_executed = 0

    async def task_to_change_variable():
        global variable_to_change_when_task_executed
        variable_to_change_when_task_executed = 1

    job = Job(task=task_to_change_variable)

    await execute_job_use_case(job)

    assert variable_to_change_when_task_executed == 1
