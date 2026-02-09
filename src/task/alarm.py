import asyncio


async def alarm(seconds, name):
    await asyncio.sleep(seconds)
    print(f"{name} ALARM!")


async def main():
    print("Таймеры запущены")
    task_1 = asyncio.create_task(alarm(0.2, "Первый"))
    task_2 = asyncio.create_task(alarm(0.1, "Второй"))
    await task_1
    await task_2

if __name__ == "__main__":
    asyncio.run(main())
