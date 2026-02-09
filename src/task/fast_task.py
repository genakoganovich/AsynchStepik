import asyncio


async def fast_task():
    print("Быстрая задача стартовала")
    await asyncio.sleep(0.1)
    print("Быстрая задача финишировала")


async def slow_task():
    print("Медленная задача стартовала")
    await asyncio.sleep(0.2)
    print("Медленная задача финишировала")


async def main():
    task_1 = asyncio.create_task(fast_task())
    task_2 = asyncio.create_task(slow_task())
    await task_1
    await task_2


if __name__ == "__main__":
    asyncio.run(main())
