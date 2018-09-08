import pytest

from aiorq.backends import get_conn, init_redis, redis_conn


pytestmark = pytest.mark.asyncio


@pytest.fixture(autouse=True)
async def setup_redis(event_loop):
    await init_redis(event_loop)
    yield

    redis = get_conn()
    await redis.flushall()


async def test_redis_conn():
    @redis_conn
    async def add_data(conn):
        await conn.set('key', 'value')

    @redis_conn
    async def get_data(conn):
        return await conn.get('key')

    await add_data()

    assert await get_data() == b'value'
