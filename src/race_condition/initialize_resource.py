import asyncio

RESOURCE_INITIALIZED = False
lock = asyncio.Lock()


async def initialize_resource():
    global RESOURCE_INITIALIZED
    async with lock:
        if not RESOURCE_INITIALIZED:
            print("Инициализация ресурса...")
            await asyncio.sleep(0.1)
            RESOURCE_INITIALIZED = True


async def main():
    await asyncio.gather(*[initialize_resource() for _ in range(5)])


if __name__ == "__main__":
    asyncio.run(main())
