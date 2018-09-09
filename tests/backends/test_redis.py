import pytest

from backends import redis_conn


pytestmark = pytest.mark.asyncio


async def test_redis_conn(redis):
    @redis_conn
    async def add_data(conn):
        await conn.set('key', 'value')

    @redis_conn
    async def get_data(conn):
        return await conn.get('key')

    await add_data()

    assert await get_data() == b'value'
