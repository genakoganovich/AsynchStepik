import asyncio

SHARED_RESOURCE = 0


async def unsafe_worker(lock):
    global SHARED_RESOURCE
    async with lock:
        value = SHARED_RESOURCE
        await asyncio.sleep(0.01)
        SHARED_RESOURCE = value + 1


async def main():
    lock = asyncio.Lock()
    await asyncio.gather(*[unsafe_worker(lock) for _ in range(10)])
    print(SHARED_RESOURCE)


if __name__ == "__main__":
    asyncio.run(main())
