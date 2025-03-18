import asyncio


async def fetch_data(id, delay):
    print(id, "start")
    await asyncio.sleep(delay)
    print(id, "end with delay ",delay)
    return {"id :":id, "data :": "some data"}


async def main():
    result = await asyncio.gather(fetch_data(1,10), fetch_data(2,6), fetch_data(3,3))

    print(result)
    for i in result:
        print(i)

asyncio.run(main())
