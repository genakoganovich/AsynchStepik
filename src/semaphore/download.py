import asyncio


async def download(file_id, semaphore):
    async with semaphore:
        await asyncio.sleep(0.1)
        return f"Файл {file_id} загружен"


async def main():
    semaphore = asyncio.Semaphore(2)
    results =  await asyncio.gather(*[download(i, semaphore) for i in range(5)])
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
