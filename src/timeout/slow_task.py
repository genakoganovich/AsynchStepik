import asyncio


async def slow_task():
    await asyncio.sleep(1)


async def main():
    try:
        await asyncio.wait_for(slow_task(), timeout=0.1)
    except asyncio.TimeoutError:
        print("Операция не уложилась в срок!")


if __name__ == "__main__":
    asyncio.run(main())
