import ray
import numpy as np
from time import sleep


@ray.remote
class Server:
    def to_text(self, seed, image):
        print("yo this is working.", image)
        sleep(1)
        return f"seed: {seed}, {image}"


if __name__ == '__main__':
    ray.init(address="auto")
