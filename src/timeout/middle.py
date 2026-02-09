import asyncio


async def inner():
    await asyncio.sleep(10)

async def middle():
    await asyncio.wait_for(inner(), timeout=2.0)


async def main():
    try:
        await asyncio.wait_for(middle(), timeout=1.0)
    except asyncio.TimeoutError:
        print("Сработал внешний тайм-аут")


if __name__ == "__main__":
    asyncio.run(main())
