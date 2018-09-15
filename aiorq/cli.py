import argparse
import asyncio

import uvloop

from backends import init_redis
from consumer import consume_queue
from queues import Queue


parser = argparse.ArgumentParser(description='Start a consumer')
parser.add_argument('-q', type=str, default='default')


async def consume(config):
    queue = Queue(id=config.q)
    loop = asyncio.get_running_loop()

    await init_redis(loop)
    while True:
        await consume_queue(queue)


if __name__ == '__main__':
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)

    args = parser.parse_args()
    loop.run_until_complete(consume(args))
