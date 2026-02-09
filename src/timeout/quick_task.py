import asyncio


async def quick_task():
    await asyncio.sleep(0.1)
    return "Успех"


async def main():
    result = await asyncio.wait_for(quick_task(), timeout=1)
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
