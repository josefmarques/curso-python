import asyncio


async def sum(a, b):
    return a + b


coro = sum(2, 3)

# EVENT LOOP = executa as tarefas assícronas

event_loop2 = asyncio.new_event_loop()
result = event_loop2.run_until_complete(coro)
print(result)
