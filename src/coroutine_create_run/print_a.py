import asyncio


async def print_a_coroutine():
    print('A')

async def print_b_coroutine():
    print('B')


async def main():
    await print_a_coroutine()
    await print_b_coroutine()


if __name__ == "__main__":
    asyncio.run(main())
