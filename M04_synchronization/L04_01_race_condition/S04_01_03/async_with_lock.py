import asyncio

COUNTER = 0
# Lock создается один раз вне корутин
lock = asyncio.Lock()


async def increment():
    global COUNTER

    # Теперь вся опасная работа происходит внутри "async with"
    async with lock:
        # --- НАЧАЛО КРИТИЧЕСКОЙ СЕКЦИИ ---
        # Только одна задача может быть здесь в один момент времени!
        temp_counter = COUNTER
        await asyncio.sleep(0)
        COUNTER = temp_counter + 1
        # --- КОНЕЦ КРИТИЧЕСКОЙ СЕКЦИИ ---


async def main():
    # Запускаем 10 задач конкурентно
    await asyncio.gather(*(increment() for _ in range(10)))


asyncio.run(main())
print(f"Итоговый счетчик: {COUNTER}")
