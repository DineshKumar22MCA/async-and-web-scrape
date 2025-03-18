import asyncio


async def fetch_data(delay):
    print("1-fetching data..")
    await asyncio.sleep(delay)
    print("1-data fetched end ")
    return {"data ": "some data"}


async def fetch_data2(delay):
    print("2-fetching data..")
    await asyncio.sleep(delay)
    print("2-data fetched end ")
    return {"data ": "some data"}


async def main():
    print("main- start process")
    task = fetch_data(5)
    result = await task
    await fetch_data2(1)
    print("main :", task)
    print("main-end ")


asyncio.run(main())
