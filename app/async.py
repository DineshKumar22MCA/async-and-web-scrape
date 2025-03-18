from flask import Flask
import asyncio

app = Flask(__name__)

@app.route("/")
async def index():
    try:
        await asyncio.sleep(3) 
        return "Hello, dineshhhh!"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run()
