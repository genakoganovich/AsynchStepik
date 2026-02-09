import asyncio


async def good_worker():
    await asyncio.sleep(1)

async def bad_worker():
    await asyncio.sleep(0.1)
    raise RuntimeError

async def main():
    try:
        await asyncio.gather(good_worker(), bad_worker())
    except RuntimeError:
        print("Поймал ошибку от gather!")


if __name__ == "__main__":
    asyncio.run(main())
