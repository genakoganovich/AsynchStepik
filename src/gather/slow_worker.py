import asyncio


async def slow_worker():
    await asyncio.sleep(0.2)
    return "Медленная работа завершена"


async def fast_worker():
    await asyncio.sleep(0.1)
    return "Быстрая работа завершена"


async def main():
    result = await asyncio.gather(
        slow_worker(),
        fast_worker(),
    )
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
