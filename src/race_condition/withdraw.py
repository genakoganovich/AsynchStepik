import asyncio

balance = 100
lock = asyncio.Lock()


async def withdraw(amount):
    global balance
    async with lock:
        if balance >= amount:
            await asyncio.sleep(0.01)
            balance -= amount
            print("Снятие успешно")
        else:
            print("Недостаточно средств")

async def main():
    global balance
    await asyncio.gather(*[withdraw(70) for _ in range(2)])
    print(balance)

if __name__ == "__main__":
    asyncio.run(main())
