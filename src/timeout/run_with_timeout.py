import asyncio



async def long_fetch():
    await asyncio.sleep(1)
    return "Данные получены"

async def run_with_timeout(coro, timeout):
    try:
        return await asyncio.wait_for(coro, timeout=timeout)
    except asyncio.TimeoutError:
        return "Тайм-аут!"


async def main():
    result = await run_with_timeout(long_fetch(), 0.1)
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
