from aiorq.backends.redis import redis_conn, init_redis
import pytest

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


@pytest.fixture(autouse=True)
async def clean_redis(event_loop):
    await init_redis(event_loop)
    yield

    @redis_conn
    async def clean(conn):
        await conn.flushall()

    await clean()


async def test_redis_conn():
    @redis_conn
    async def add_data(conn):
        await conn.set('key', 'value')

    @redis_conn
    async def get_data(conn):
        return await conn.get('key')

    await add_data()

    assert await get_data() == b'value'
