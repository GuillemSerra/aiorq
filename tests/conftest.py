import pytest

from backends import get_conn, init_redis, stop_redis


@pytest.fixture
async def redis(event_loop):
    await init_redis(event_loop)
    redis = get_conn()
    yield redis

    await redis.flushall()
    await stop_redis()
