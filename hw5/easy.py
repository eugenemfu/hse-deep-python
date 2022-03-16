import asyncio
import aiohttp
import argparse
import os
from pathlib import Path
import numpy as np


URL = "https://picsum.photos/200/300"


async def download_image(session, target):
    async with session.get(URL) as img:
        img_ = await img.read()
        with open(target, "wb") as f:
            f.write(img_)


async def download_images(n, folder):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(n):
            target = folder / (str(np.random.randint(n * 1000)) + ".png")
            tasks.append(asyncio.create_task(download_image(session, target)))
        return await asyncio.gather(*tasks)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-n", type=int, default=5)
    argparser.add_argument("-f", type=str, default="artifacts/easy")
    args = argparser.parse_args()
    os.makedirs(args.f, exist_ok=True)
    asyncio.run(download_images(n=args.n, folder=Path(args.f)))