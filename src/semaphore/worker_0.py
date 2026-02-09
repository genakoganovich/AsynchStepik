import asyncio


active_tasks = 0
max_active_tasks = 0
semaphore = asyncio.Semaphore(3)


async def worker():
    global active_tasks
    global max_active_tasks
    async with semaphore:
        active_tasks += 1
        max_active_tasks = active_tasks if active_tasks > max_active_tasks else max_active_tasks
        await asyncio.sleep(0.1)
        active_tasks -= 1

async def main():
    global max_active_tasks
    await asyncio.gather(*[worker() for _ in range(10)])
    print(max_active_tasks)


if __name__ == "__main__":
    asyncio.run(main())
