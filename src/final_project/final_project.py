import asyncio
import random


async def generate_data(output_queue, items_count):
    for i in range(1, items_count + 1):
        var = {'id': i, 'status': 'raw'}
        await asyncio.sleep(random.uniform(0, 0.5))
        print(f"[ГЕНЕРАТОР] Сгенерированы данные: {var}")
        await output_queue.put(var)

async def process_data(worker_id, input_queue, output_queue):
    while True:
        pass


async def aggregate_results(input_queue, items_count):
    pass
