import asyncio


async def timer(delay, value):
    await asyncio.sleep(delay)
    return value


async def main():
    result = await asyncio.gather(
        timer(0.2, "A"),
        timer(0.1, "B"),
    )
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
