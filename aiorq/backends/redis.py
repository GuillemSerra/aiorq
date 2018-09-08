import asyncio
import functools
from typing import Coroutine

from aioredis import create_redis_pool


CONFIG = {
    'URI': 'redis://localhost',
    'POOL_MIN_SIZE': 5,
    'POOL_MAX_SIZE': 20,
}
pool = None


async def init_redis(loop: asyncio.BaseEventLoop):
    global pool
    pool = await create_redis_pool(CONFIG['URI'],
                                   minsize=CONFIG['POOL_MIN_SIZE'],
                                   maxsize=CONFIG['POOL_MAX_SIZE'],
                                   loop=loop)


async def stop_redis():
    global pool
    await pool.close()


def redis_conn(f: Coroutine) -> Coroutine:
    @functools.wraps(f)
    async def wrapper(*args, **kwargs):
        return await f(pool, *args, **kwargs)

    return wrapper


def get_conn():
    return pool
