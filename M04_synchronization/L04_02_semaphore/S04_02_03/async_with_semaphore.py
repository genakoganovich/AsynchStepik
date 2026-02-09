import asyncio

# Создаем семафор, который пропустит не более 10 задач одновременно
semaphore = asyncio.Semaphore(10)

async def make_request(request_num):
    async with semaphore:
        # --- НАЧАЛО ОГРАНИЧЕННОЙ ЗОНЫ ---
        # Этот код будет выполняться одновременно
        # не более чем для 10 задач.
        print(f"Запрос #{request_num} 'заехал на парковку'")
        await asyncio.sleep(1) # Имитация работы
        # --- КОНЕЦ ОГРАНИЧЕННОЙ ЗОНЫ ---
    print(f"Запрос #{request_num} 'выехал с парковки'")

