import asyncio
import random


async def generate_data(output_queue, items_count):
    for i in range(1, items_count + 1):
        item = {'id': i, 'status': 'raw'}
        await asyncio.sleep(random.uniform(0, 0.5))
        print(f"[ГЕНЕРАТОР] Сгенерированы данные: {item}")
        await output_queue.put(item)

async def process_data(worker_id, input_queue, output_queue):
    try:
        while True:
            item = await input_queue.get()
            await asyncio.sleep(random.uniform(0.1, 1.0))
            item['status'] = 'processed'
            print(f"[ВОРКЕР {worker_id}] Обработаны данные: {item}")
            await output_queue.put(item)
            input_queue.task_done()
    except asyncio.CancelledError:
        raise


async def aggregate_results(input_queue, items_count):
    for _ in range(items_count):
        item = await input_queue.get()
        print(f"[АГРЕГАТОР] Получен результат: {item}")


async def main():
    TOTAL_ITEMS = 10
    WORKERS_COUNT = 3
    raw_data_queue = asyncio.Queue()
    processed_data_queue = asyncio.Queue()

    # Запускаем Агрегатор, который ждет все N результатов
    aggregator_task = asyncio.create_task(aggregate_results(processed_data_queue, TOTAL_ITEMS))

    # Запускаем несколько Воркеров
    worker_tasks = []
    for i in range(WORKERS_COUNT):
        task = asyncio.create_task(process_data(i, raw_data_queue, processed_data_queue))
        worker_tasks.append(task)

    # Эта команда будет "держать" main, пока все данные не будут созданы
    await generate_data(raw_data_queue, TOTAL_ITEMS)
    await aggregator_task
    for task in worker_tasks:
        task.cancel()

    # Собираем отмененные задачи, чтобы обработать CancelledError
    await asyncio.gather(*worker_tasks, return_exceptions=True)

if __name__ == '__main__':
    asyncio.run(main())