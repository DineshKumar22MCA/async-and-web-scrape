import asyncio


async def set_future_result(future, value):
    print("start set_future_result")
    await asyncio.sleep(3)
    future.set_result(value)
    print("set future result value : ",value)
    print("end set_future_result")


async def main():
    loop = asyncio.get_running_loop()
    print("loop : ",loop)
    print(type(loop))
    future = loop.create_future()
    print("future : ",future)
    print(type(future))
    
    asyncio.create_task(set_future_result(future, "future result is ready"))

    result = await future
    print("main future result : ", result)


asyncio.run(main())
