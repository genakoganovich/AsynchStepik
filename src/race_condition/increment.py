import asyncio

COUNTER = 0
lock = asyncio.Lock()


async def increment():
    async with lock:
        global COUNTER
        COUNTER += 1


async def main():
    await asyncio.gather(*[increment() for _ in range(100)])
    print(COUNTER)


if __name__ == "__main__":
    asyncio.run(main())
