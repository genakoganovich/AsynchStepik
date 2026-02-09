import asyncio
import time


async def wait_and_print():
    print("Начинаю долгое ожидание...")

    # Вот она, точка приостановки!
    # Код "замрет" здесь, но не заблокирует программу.
    await asyncio.sleep(2)

    print("...ожидание завершено!")


async def main():
    print("Программа запущена.")
    start_time = time.time()

    # Вызываем и ЖДЕМ (await), пока wait_and_print не завершится.
    await wait_and_print()

    end_time = time.time()
    print(f"Программа завершена за {end_time - start_time:.2f} секунд.")


# asyncio.run() - это специальная функция, которая создает
# Цикл событий, запускает в нем нашу главную корутину 'main'
# и ждет ее завершения. Это точка входа в асинхронный мир.
asyncio.run(main())