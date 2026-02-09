import asyncio


async def task_a(semaphore):
    async with semaphore:
        print("A start")
        await asyncio.sleep(0.1)
        print("A end")

async def task_b(semaphore):
    async with semaphore:
        print("B start")
        await asyncio.sleep(0.1)
        print("B end")


async def main():
    semaphore = asyncio.Semaphore(1)
    await asyncio.gather(task_a(semaphore), task_b(semaphore))


if __name__ == "__main__":
    asyncio.run(main())
