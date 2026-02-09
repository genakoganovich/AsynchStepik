import asyncio


async def print_message():
    await asyncio.sleep(0.1)
    print("Задача выполнена!")


async def main():
    task = asyncio.create_task(print_message())
    print("Задача запущена, ждем...")
    await task

if __name__ == "__main__":
    asyncio.run(main())
