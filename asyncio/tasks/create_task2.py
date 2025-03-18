import asyncio


async def fetch_data(id, delay):
    print("fetch data co-rountine id : ", id)
    await asyncio.sleep(delay)
    print("end : ", id , "with" ,delay , "sec")
    return {"id :":id, "data :": "some data"}



async def main():
    task1 = asyncio.create_task(fetch_data(1, 10))
    task2 = asyncio.create_task(fetch_data(2, 6))

    result1 = await task1
    result2 = await task2

    task3 = asyncio.create_task(fetch_data(3, 3))

    result3 = await task3

    print(result1)
    print(result2)
    print(result3)


asyncio.run(main())
