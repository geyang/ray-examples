# from asyncio import sleep
import asyncio
from time import sleep
import ray
import numpy as np


# @ray.remote(num_gpus=1)
@ray.remote
class Server:
    async def to_text(self, seed, image):
        print("starting", image)
        # await sleep(0.1)
        await asyncio.sleep(1)
        sleep(1)
        print(f"seed {seed} done.")
        return f"seed: {seed}, {image}"


# if __name__ == '__main__':
#     ray.init(address="auto")
