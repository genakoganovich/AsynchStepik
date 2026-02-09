import asyncio


async def square(n):
    return n * n


async def main():
    numbers = [1, 2, 3, 4, 5]
    results = await asyncio.gather(*[square(i) for i in numbers])
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
