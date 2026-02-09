import asyncio


async def fetch_data(data):
    return data


async def main():
    results = await asyncio.gather(
        fetch_data("apple"),
        fetch_data(100),
        fetch_data(True),
    )
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
