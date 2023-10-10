import asyncio
from functools import lru_cache
from time import sleep

import ray
import numpy as np
from PIL import Image

from main import Server


image = Image.open("example.png")

@lru_cache
def get_remote():
    ray.init(address="localhost:6379")
    return Server.options(max_concurrency=10).remote()

async def client():
    all_tasks = []
    for i in range(10):
        remote = get_remote()
        seed = i
        result = await remote.to_text.remote(seed, image)
        print("result:", result)
    #     feature = remote.to_text.remote(seed, image)
    #     all_tasks.append(feature)
    #
    # print("waiting for all tasks to finish")
    # sleep(10)
    # ray.get(all_tasks)
    print("all tasks finished")


if __name__ == '__main__':
    asyncio.run(client())
