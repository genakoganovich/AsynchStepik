import asyncio


async def success_task():
    return "Успех"

async def failure_task():
    raise ValueError


async def main():
    result = await asyncio.gather(success_task(), failure_task(), return_exceptions=True)
    print(result[0])
    print(isinstance(result[1], ValueError))


if __name__ == "__main__":
    asyncio.run(main())
