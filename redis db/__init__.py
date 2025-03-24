
import redis


redis_instance = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

try:
    response = redis_instance.ping()
    if response:
        print("Successfully connected to Redis!")
        print(response)
except redis.ConnectionError:
    print("Failed to connect to Redis.")

redis_instance.set("name","dinesh")
name = redis_instance.get("name")

print(name)
print(type(name))
print(type(redis_instance.get("name")))


redis_instance.set("name","virat")
name = redis_instance.get("name")

print(name)

keys = redis_instance.keys('*')
print(keys)

dele = redis_instance.delete("name")
print(dele)
print(keys)

print(name)


print(redis_instance.close())
connection = redis_instance.close()
print(connection)
if connection is None:
    print("connection closed")