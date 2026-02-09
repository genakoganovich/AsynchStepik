import asyncio


async def worker(delay):
    await asyncio.sleep(delay)
    return f"Завершено за {delay}с"


async def main():
    result = await asyncio.gather(
        asyncio.wait_for(worker(0.1), timeout=0.2),
        asyncio.wait_for(worker(0.3), timeout=0.2),
        return_exceptions=True)
    print(result[0])
    print(isinstance(result[1], TimeoutError))

if __name__ == "__main__":
    asyncio.run(main())
