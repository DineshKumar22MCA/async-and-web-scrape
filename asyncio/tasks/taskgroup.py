import asyncio


async def fetch_data(id, delay):
    print(id, "start")
    await asyncio.sleep(delay)
    print(id, "end with delay ",delay)
    return {"id :":id, "data :": "some data"}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for id, delay in enumerate([1,2,3], start=1):
            task = tg.create_task(fetch_data(id, delay))
            tasks.append(task)

    
    result = [i.result() for i in tasks]

    for i in result:
        print(i)


asyncio.run(main())
