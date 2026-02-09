import asyncio


async def worker_a(lock):
    async with lock:
        print("Работа A: Начало")
        await asyncio.sleep(0.1)
        print("Работа A: Конец")

async def worker_b(lock):
    async with lock:
        print("Работа B: Начало")
        await asyncio.sleep(0.1)
        print("Работа B: Конец")

async def main():
    lock = asyncio.Lock()
    await asyncio.gather(worker_a(lock), worker_b(lock))


if __name__ == "__main__":
    asyncio.run(main())
