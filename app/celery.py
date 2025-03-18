from flask import Flask
from celery import Celery


app = Flask(__name__)

app.config["CELERY_BROKER_URL"] = "redis://localhost:6379/0"
app.config["CELERY_RESULT_BACKEND"] = "redis://localhost:6379/0"

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config["CELERY_BROKER_URL"])
    celery.conf.update(app.config)
    return celery

celery = make_celery(app)


@celery.task
def long_task():
    import time
    time.sleep(5)
    return "Task completed!"


@app.route("/")
def start_task():
    task = long_task.delay()  
    return f"Task {task.id} started!"


if __name__ == "__main__":
    app.run(debug=True)
