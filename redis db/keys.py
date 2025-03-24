import redis


try:
    red = redis.Redis(host="127.0.0.1", port=6379)

    red.set("name","kohli")
    keys = red.keys('*')
    print(keys)

    red.delete("name")

    keys = red.keys('*')
    print(keys)

    # hashing values
    user_data ={
        "name": "virat",
        "age": 26,
        "email": "dk@gmail.com" 
    }

    red.hset("user", mapping=user_data)
    user_data = red.hgetall("user")
    print(user_data)

    #store as list
    red.rpush('task_queue', 'task1', 'task2', 'task3')
    tasks = red.lrange('task_queue', 0, -1)
    print(tasks)

    red.sadd('task_set', 'task1', 'task2', 'task3')
    tasks = red.smembers('task_set')
    print(tasks)

    #store as set
    red.sadd('unique_visitors', 'user1', 'user2', 'user3')
    visitors = red.smembers('unique_visitors')
    print(visitors)

    red.set('session_token', 'abc123')
    red.expire('session_token', 10)

    token = red.get('session_token')
    print(token)

    red.set('session_token', 'abc123', ex=3600)

    pipe = red.pipeline()
    pipe.set('foo', 5)
    pipe.set('bar', 18.5)
    pipe.set('blee', "hello world!")
    pipe.execute()



except Exception as e:
    print(str(e))
finally:
    connection = red.close()
    if connection is None:
        print("redis connection closed")
