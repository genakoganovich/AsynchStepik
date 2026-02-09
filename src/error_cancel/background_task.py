import asyncio
from asyncio import gather


async def background_task():
    await asyncio.sleep(10)
    print("Фоновая задача завершена")


async def main_logic(bg_task):
    print("Основная логика: Начало")
    await asyncio.sleep(0.1)
    raise ValueError("Произошел сбой!")
    print("Основная логика: Конец")

async def main():
    task = asyncio.create_task(background_task())
    try:
        await asyncio.gather(main_logic(task), return_exceptions=True)
    finally:
        task.cancel()
        await asyncio.sleep(0)
        print("Очистка: Фоновая задача отменена.")


if __name__ == "__main__":
    asyncio.run(main())
