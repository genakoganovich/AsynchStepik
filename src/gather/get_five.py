import asyncio


async def get_five():
    return 5


async def get_ten():
    return 10


async def main():
    results = await asyncio.gather(
        get_five(),
        get_ten(),
    )
    print(sum(results))



if __name__ == "__main__":
    asyncio.run(main())
