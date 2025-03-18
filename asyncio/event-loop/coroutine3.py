import asyncio


async def fetch_data(delay, id):
    print("1-fetching data..", id)
    await asyncio.sleep(delay)
    print("1-data fetched", id)
    return {"data ": "some data", "id :": id}


async def fetch_data2(delay, id):
    print("2-fetching data..", id)
    await asyncio.sleep(delay)
    print("2-data fetched", id)
    return {"data ": "some data", "id :": id}


async def main():
    print("main- start process")
    task1 = fetch_data(5, 5)
    task2 = fetch_data2(2, 10)
    print(task1, task2)

    result = await task1
    print("main :", result)

    result2 = await task2
    print("main :", result2)
    
    print("main-end ")


asyncio.run(main())
