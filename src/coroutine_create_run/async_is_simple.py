import asyncio

async def print_simple_coroutine():
    print("Асинхронность - это просто!")

async def main():
    await print_simple_coroutine()

asyncio.run(main())