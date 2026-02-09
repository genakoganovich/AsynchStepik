import asyncio


async def get_value_coroutine(value, delay):
    await asyncio.sleep(delay)
    return value


async def main():
    a = await get_value_coroutine(value=5, delay=0.1)
    b = await get_value_coroutine(value=10, delay=0.2)
    print(a + b)

if __name__ == "__main__":
    asyncio.run(main())
