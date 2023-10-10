import ray
import numpy as np
from PIL import Image

from main import Server

ray.init(address="localhost:6379")

image = Image.open("example.png")

remote = Server.remote()
for i in range(10):
    seed = i
    feature = remote.to_text.remote(seed, image)
    result = ray.get(feature)
    print(result)


