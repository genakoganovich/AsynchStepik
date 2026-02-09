import asyncio


async def simulate_operation_coroutine():
    print("Начало операции")
    await asyncio.sleep(0.5)
    print("Конец операции")


async def main():
    await simulate_operation_coroutine()


if __name__ == "__main__":
    asyncio.run(main())
