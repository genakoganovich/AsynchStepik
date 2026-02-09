def regular_function():
    return "Я обычная функция!"

async def coroutine_function():
    return "Я особенная функция-корутина!"

result = regular_function()
print(result)
# Вывод: Я обычная функция!

result = coroutine_function()
print(result)