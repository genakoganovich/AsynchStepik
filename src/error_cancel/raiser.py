import asyncio


async def raiser():
    raise ValueError("Произошла ошибка!")


async def main():
    try:
        await raiser()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(main())
