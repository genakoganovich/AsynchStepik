import asyncio


async def long_runner():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("Задача отменена!")


async def main():
    task = asyncio.create_task(long_runner())
    await asyncio.sleep(0.1)
    task.cancel()
    await asyncio.gather(task, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())
