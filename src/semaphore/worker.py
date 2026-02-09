import asyncio

preparing_count = 0
max_preparing = 0
working_count = 0
max_working = 0
lock = asyncio.Lock()


async def worker(worker_id, semaphore):
    global preparing_count
    global max_preparing
    global working_count
    global max_working

    # Подготовка
    async with lock:
        preparing_count += 1
        max_preparing = preparing_count if preparing_count > max_preparing else max_preparing
    await asyncio.sleep(0.1)
    # Работа
    async with semaphore:
        async with lock:
            working_count += 1
            max_working = working_count if working_count > max_working else max_working
        await asyncio.sleep(0.2)
        async with lock:
            working_count -= 1


async def main():
    global max_preparing
    global max_working
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*[worker(i, semaphore) for i in range(4)])
    print(max_preparing)
    print(max_working)


if __name__ == "__main__":
    asyncio.run(main())
