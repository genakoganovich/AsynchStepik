import asyncio


async def worker(n):
    print(f"Задача {n} выполнена.")


async def main():
    worker_tasks = []
    for i in range(3):
        worker_tasks.append(asyncio.create_task(worker(i)))
    print("Все задачи запущены.")

if __name__ == "__main__":
    asyncio.run(main())
