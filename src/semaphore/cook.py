import asyncio

active_cooks = 0
max_concurrent_cooks = 0
lock = asyncio.Lock()


async def cook(order, semaphore, cook_time):
    global active_cooks
    global max_concurrent_cooks
    global lock
    end = "а" if order.endswith("а") else ""
    print(f"[Повар] Взял заказ: {order}, ждет свободную плиту.")
    await asyncio.sleep(0)

    async with semaphore:
        async with lock:
            active_cooks += 1
            max_concurrent_cooks = active_cooks if active_cooks > max_concurrent_cooks else max_concurrent_cooks

        print(f"{order} готовится. Поваров на кухне: {active_cooks}")
        await asyncio.sleep(cook_time)
        async with lock:
            active_cooks -= 1
        print(f"{order} готов{end}! Поваров на кухне: {active_cooks}")



async def main():
    global max_concurrent_cooks
    semaphore = asyncio.Semaphore(3)
    orders_with_times = {
        "Паста": 0.1,
        "Суп": 0.2,
        "Салат": 0.3,
        "Стейк": 0.15,
        "Рыба": 0.25
    }
    await asyncio.gather(*[cook(key, semaphore, value) for key, value in orders_with_times.items()])
    print("\n--- Результаты смены ---")
    print("Все заказы выполнены.")
    print(f"Максимальное число поваров на кухне одновременно: {max_concurrent_cooks}")

if __name__ == "__main__":
    asyncio.run(main())
